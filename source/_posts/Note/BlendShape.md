# Blendshape学习笔记

## Blendshape(Morph Target动画)

Blendshapes泛指3D定点动画的制作方式 (Maya里面称之为 blend shapes ，而3DS Max里称之为morph targets) ，在3D动画中用的比较多，尤其是人脸动画的制作，通过blendshape来驱动角色的面部表情。

用在脸部动画制作时，blendshape可以被称之为**脸部特征，表情基准，定位符**等等。这里要引入一个`FACS`的概念，可以简单理解为将脸部进行合理化的分区标准。

> “表情这个东西看起来是一个无限多可能的东西，怎么能够计算expression呢？
>
> 这就带来了Blendshapes——一组组成整体表情的基准（数量可以有十几个、50个、100+、 200+，越多就越细腻)。我们可以使用这一组基准通过线性组合来计算出整体的expression，用公式来说就是  ，其中e是expression，B是一组表情基准，d是对应的系数（在这一组里面的权重），b是neutral。” 
>
> -- From https://zhuanlan.zhihu.com/p/78174706



## BlendShape系数介绍

在ARKit中，对表情特征位置定义了52组运动blendshape系数(
https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation)，每个blendshape系数代表一种表情定位符，表情定位符定义了特定表情属性，如mouthSmileLeft、mouthSmileRight等，与其对应的blendshape系数则表示表情运动范围。这52组blendshape系数极其描述如下表所示。

![Blendshape](https://p3-sign.toutiaoimg.com/pgc-image/984d8d76878441c3a8402f788ef6e46f~noop.image?_iz=58558&from=article.pc_detail&lk3s=953192f4&x-expires=1710668214&x-signature=qI8vU39X63te%2BVNdO78uBFphwK0%3D)

每一个blendshape系数的取值范围为0～1的浮点数。以jawOpen为例，当认为用户的嘴巴完全闭紧时，返回的jawOpen系数为0。当认为用户的嘴巴张开至最大时，返回的jawOpen系数为1。

每一个blendshape系数的取值范围为0～1的浮点数。以jawOpen为例，当认为用户的嘴巴完全闭紧时，返回的jawOpen系数为0。当认为用户的嘴巴张开至最大时，返回的jawOpen系数为1。

![](https://p6-sign.toutiaoimg.com/pgc-image/2c8cbd123e00470e95500a8ae62da605~noop.image?_iz=58558&from=article.pc_detail&lk3s=953192f4&x-expires=1710668214&x-signature=UHPhjWP4v96kbtfJzF97Z%2Bp3klc%3D)



在用户完全闭嘴与嘴张到最大之间的过渡状态，jawOpen会根据用户嘴张大的幅度返回一个0～1的插值。

![](https://p3-sign.toutiaoimg.com/pgc-image/8e8d980b8d69461fb5d2efbc50e47d47~noop.image?_iz=58558&from=article.pc_detail&lk3s=953192f4&x-expires=1710668214&x-signature=sFNMeBoNY3ZFfiO%2BRSjR8uGECIw%3D)



## 脸部动捕的使用

### ARKit 脸部与Vive脸部blendshape基准对比

|        | ARKit（52） | Extra      | VIVE（52） | Extra         |
| ------ | ----------- | ---------- | ---------- | ------------- |
| Brow   | 5           |            | 0          |               |
| Eye    | 13          |            | 14         | Eye Frown + 1 |
| Cheek  | 3           |            | 3          |               |
| Nose   | 2           |            | 0          |               |
| Jaw    | 4           |            | 4          |               |
| Mouth  | 24          |            | 20         | O shape - 1   |
| Tongue | 1           | Tongue + 7 | 11         |               |
| Sum    | 52          | 59         | 52         | 52            |



### ARKit的52个Blendshape表情基准组

可以看ARKit Face Blendshapes的照片和3D模型示例：https://arkit-face-blendshapes.com/

| CC3  | ARKit Name 表情基准/定位符 | ARKit Picture                                                | CC3 Picture                                                  |
| ---- | -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| A01  | browInnerUp                | ![img](https://static.wixstatic.com/media/64c63b_4cc12dd62ef8484986eebe9739f4eac9~mv2.png/v1/fill/w_252,h_178,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_4cc12dd62ef8484986eebe9739f4eac9~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_fc0c248f4f6f46dda26eda66865678d2~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_fc0c248f4f6f46dda26eda66865678d2~mv2.png) |
| A02  | browDownLeft               | ![img](https://static.wixstatic.com/media/64c63b_18a57dc078214abea520f25ad6dfb02a~mv2.png/v1/fill/w_252,h_175,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_18a57dc078214abea520f25ad6dfb02a~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_9d780933931b469991ae0d4ddf105045~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_9d780933931b469991ae0d4ddf105045~mv2.png) |
| A03  | browDownRight              | ![img](https://static.wixstatic.com/media/64c63b_105d6dd9d7c44394b96b242e6d9d580b~mv2.png/v1/fill/w_252,h_175,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_105d6dd9d7c44394b96b242e6d9d580b~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_d9943f7163414286809edef7c3bf2de7~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_d9943f7163414286809edef7c3bf2de7~mv2.png) |
| A04  | browOuterUpLeft            | ![img](https://static.wixstatic.com/media/64c63b_e7fe8581da2540a3bd7dfc39c874dd61~mv2.png/v1/fill/w_252,h_175,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_e7fe8581da2540a3bd7dfc39c874dd61~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_c7234589721d4ddda4e2fcb1a9e0aa97~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_c7234589721d4ddda4e2fcb1a9e0aa97~mv2.png) |
| A05  | browOuterUpRight           | ![img](https://static.wixstatic.com/media/64c63b_1fb29f740ff74e8aabadc3769c86501a~mv2.png/v1/fill/w_252,h_175,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_1fb29f740ff74e8aabadc3769c86501a~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_4aefd80dd4c548669d5ba80e4da639eb~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_4aefd80dd4c548669d5ba80e4da639eb~mv2.png) |
| A06  | eyeLookUpLeft              | ![img](https://static.wixstatic.com/media/64c63b_697a02a504c84d5f9e316172849bb6d0~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_697a02a504c84d5f9e316172849bb6d0~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_48e3b55ee9ca40f9aec9be8b35c403b0~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_48e3b55ee9ca40f9aec9be8b35c403b0~mv2.png) |
| A07  | eyeLookUpRight             | ![img](https://static.wixstatic.com/media/64c63b_84cacf1f990a4e5c874c084a1ea626b3~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_84cacf1f990a4e5c874c084a1ea626b3~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_c879b6cca2ce4f8aa2385864c1fb9389~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_c879b6cca2ce4f8aa2385864c1fb9389~mv2.png) |
| A08  | eyeLookDownLeft            | ![img](https://static.wixstatic.com/media/64c63b_d229ef398f3547be93a1a59563520e81~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_d229ef398f3547be93a1a59563520e81~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_d6c6c94e3cee43db8ae9d6f36fc1a689~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_d6c6c94e3cee43db8ae9d6f36fc1a689~mv2.png) |
| A09  | eyeLookDownRight           | ![img](https://static.wixstatic.com/media/64c63b_67a1674b6d584344b7ea77843f72be27~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_67a1674b6d584344b7ea77843f72be27~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_ca0dbf25d9f74085809cdcd0742ede35~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_ca0dbf25d9f74085809cdcd0742ede35~mv2.png) |
| A10  | eyeLookOutLeft             | ![img](https://static.wixstatic.com/media/64c63b_b4257aa18f754427a593064e71aa97fd~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_b4257aa18f754427a593064e71aa97fd~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_d24fd04ef2d64db18c31b90eccd5f1a9~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_d24fd04ef2d64db18c31b90eccd5f1a9~mv2.png) |
| A11  | eyeLookInLeft              | ![img](https://static.wixstatic.com/media/64c63b_03368853adeb4b8599da5451033cd809~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_03368853adeb4b8599da5451033cd809~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_049433ce862e44c4a5f96bcf0ad13bd0~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_049433ce862e44c4a5f96bcf0ad13bd0~mv2.png) |
| A12  | eyeLookInRight             | ![img](https://static.wixstatic.com/media/64c63b_6e67745f7867402398390ce18a9f2882~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_6e67745f7867402398390ce18a9f2882~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_803074453832444d8dec710711196559~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_803074453832444d8dec710711196559~mv2.png) |
| A13  | eyeLookOutRight            | ![img](https://static.wixstatic.com/media/64c63b_b54a5b6f123244d98eadbded8c29a8c3~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_b54a5b6f123244d98eadbded8c29a8c3~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_2e7b0fed966d453fa0a8dffaabeaf769~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_2e7b0fed966d453fa0a8dffaabeaf769~mv2.png) |
| A14  | eyeBlinkLeft               | ![img](https://static.wixstatic.com/media/64c63b_0b68b26a666a49da843b6a47c4579b46~mv2.png/v1/fill/w_252,h_175,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_0b68b26a666a49da843b6a47c4579b46~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_b46d50b28b5d40feba9a496b1ead4a5c~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_b46d50b28b5d40feba9a496b1ead4a5c~mv2.png) |
| A15  | eyeBlinkRight              | ![img](https://static.wixstatic.com/media/64c63b_65e50badaa854262a87329394a87484c~mv2.png/v1/fill/w_252,h_175,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_65e50badaa854262a87329394a87484c~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_9113137c91934bdbab3fb26756e84783~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_9113137c91934bdbab3fb26756e84783~mv2.png) |
| A16  | eyeSquintLeft              | ![img](https://static.wixstatic.com/media/64c63b_7b9132e314d6404097f212401559e9c4~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_7b9132e314d6404097f212401559e9c4~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_0cccb71728de47e5a7f63fe9bc70bcaf~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_0cccb71728de47e5a7f63fe9bc70bcaf~mv2.png) |
| A17  | eyeSquintRight             | ![img](https://static.wixstatic.com/media/64c63b_8cc99b12de914fe882c19229ce2a91da~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_8cc99b12de914fe882c19229ce2a91da~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_8445ac0161fe400ab28591fb6b0b1f56~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_8445ac0161fe400ab28591fb6b0b1f56~mv2.png) |
| A18  | eyeWideLeft                | ![img](https://static.wixstatic.com/media/64c63b_0c87ac4e4c5d4d5f9639523c82aa9d43~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_0c87ac4e4c5d4d5f9639523c82aa9d43~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_c097966492c3496cabf1d84455d7144d~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_c097966492c3496cabf1d84455d7144d~mv2.png) |
| A19  | eyeWideRight               | ![img](https://static.wixstatic.com/media/64c63b_3157fc370d064da9926027034e8220d6~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_3157fc370d064da9926027034e8220d6~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_24dc2c84e19b436a97fd2db6044f439c~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_24dc2c84e19b436a97fd2db6044f439c~mv2.png) |
| A20  | cheekPuff                  | ![img](https://static.wixstatic.com/media/64c63b_de4df8062c5f47ca9cd322b75b535705~mv2.png/v1/fill/w_252,h_172,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_de4df8062c5f47ca9cd322b75b535705~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_27548c426f1b47ae834c757417e03269~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_27548c426f1b47ae834c757417e03269~mv2.png) |
| A21  | cheekSquintLeft            | ![img](https://static.wixstatic.com/media/64c63b_70520c1a1c374ff3855cb8dfa7450b8b~mv2.png/v1/fill/w_252,h_175,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_70520c1a1c374ff3855cb8dfa7450b8b~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_d769bd2ef0104030818ed7a156ee2a2e~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_d769bd2ef0104030818ed7a156ee2a2e~mv2.png) |
| A22  | cheekSquintRight           | ![img](https://static.wixstatic.com/media/64c63b_2f82d4db05764690b33001da1d138f20~mv2.png/v1/fill/w_252,h_175,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_2f82d4db05764690b33001da1d138f20~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_49752693e89a4293982b5e023a0e1c75~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_49752693e89a4293982b5e023a0e1c75~mv2.png) |
| A23  | noseSneerLeft              | ![img](https://static.wixstatic.com/media/64c63b_843177402d2545d1a1f0a97e848df91c~mv2.png/v1/fill/w_252,h_178,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_843177402d2545d1a1f0a97e848df91c~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_9855bb8e50f54f638d4bc321dd3caa45~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_9855bb8e50f54f638d4bc321dd3caa45~mv2.png) |
| A24  | noseSneerRight             | ![img](https://static.wixstatic.com/media/64c63b_8ee42dc6d8e443a0858e0c65ce56cc74~mv2.png/v1/fill/w_252,h_179,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_8ee42dc6d8e443a0858e0c65ce56cc74~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_edd25cffbf1249d89bb0f6c5a95b76e5~mv2.png/v1/fill/w_241,h_217,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_edd25cffbf1249d89bb0f6c5a95b76e5~mv2.png) |
| A25  | jawOpen                    | ![img](https://static.wixstatic.com/media/64c63b_aca391d5eb744a76b18d6ced31904111~mv2.png/v1/fill/w_267,h_192,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_aca391d5eb744a76b18d6ced31904111~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_f14421d8adb1461ea32ca31bd3cac7be~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_f14421d8adb1461ea32ca31bd3cac7be~mv2.png) |
| A26  | jawForward                 | ![img](https://static.wixstatic.com/media/64c63b_a199113be0f9418f8c729d9a7e7b4e49~mv2.png/v1/fill/w_267,h_183,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_a199113be0f9418f8c729d9a7e7b4e49~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_df9963f3452c4ce1bd1b6829a8045112~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_df9963f3452c4ce1bd1b6829a8045112~mv2.png) |
| A27  | jawLeft                    | ![img](https://static.wixstatic.com/media/64c63b_2642a61cdd0241f9ba24339873003125~mv2.png/v1/fill/w_267,h_183,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_2642a61cdd0241f9ba24339873003125~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_0de7a40c68654461be74016c2e29cf02~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_0de7a40c68654461be74016c2e29cf02~mv2.png) |
| A28  | jawRight                   | ![img](https://static.wixstatic.com/media/64c63b_2838229bffe74a5abe7d25d9c6e398ca~mv2.png/v1/fill/w_267,h_183,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_2838229bffe74a5abe7d25d9c6e398ca~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_2f51f3993bed441b89b9b493a1f2e86b~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_2f51f3993bed441b89b9b493a1f2e86b~mv2.png) |
| A29  | mouthFunnel                | ![img](https://static.wixstatic.com/media/64c63b_d2719d8d83524b52a735296f0dfbf092~mv2.png/v1/fill/w_267,h_183,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_d2719d8d83524b52a735296f0dfbf092~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_e2b4d7681dcf4b1faf34e3c5b57dd3ac~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_e2b4d7681dcf4b1faf34e3c5b57dd3ac~mv2.png) |
| A30  | mouthPucker                | ![img](https://static.wixstatic.com/media/64c63b_7771a95fb2ae4afeb885b7a684e3f249~mv2.png/v1/fill/w_267,h_183,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_7771a95fb2ae4afeb885b7a684e3f249~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_e553a24166984303920d5ec9ce1de6d6~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_e553a24166984303920d5ec9ce1de6d6~mv2.png) |
| A31  | mouthLeft                  | ![img](https://static.wixstatic.com/media/64c63b_d2e30cadc9b443f6993ee48d99ffb9c8~mv2.png/v1/fill/w_267,h_183,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_d2e30cadc9b443f6993ee48d99ffb9c8~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_76b134e6564749fcaf6e036a6dc53517~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_76b134e6564749fcaf6e036a6dc53517~mv2.png) |
| A32  | mouthRight                 | ![img](https://static.wixstatic.com/media/64c63b_ef34b0cf15c541058052d74870f95a11~mv2.png/v1/fill/w_267,h_183,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_ef34b0cf15c541058052d74870f95a11~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_332e51118068490cbb932bc8b3880895~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_332e51118068490cbb932bc8b3880895~mv2.png) |
| A33  | mouthRollUpper             | ![img](https://static.wixstatic.com/media/64c63b_5c93c56f5d9e4698a86160047452fdae~mv2.png/v1/fill/w_267,h_183,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_5c93c56f5d9e4698a86160047452fdae~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_f86e02c72dcd4e27b5fafc3e7cbf5098~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_f86e02c72dcd4e27b5fafc3e7cbf5098~mv2.png) |
| A34  | mouthRollLower             | ![img](https://static.wixstatic.com/media/64c63b_8d2d50c4784b4f4a881264f9e806b26e~mv2.png/v1/fill/w_267,h_183,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_8d2d50c4784b4f4a881264f9e806b26e~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_f6ce7f1df803456fb25b77533ec5c1a9~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_f6ce7f1df803456fb25b77533ec5c1a9~mv2.png) |
| A35  | mouthShrugUpper            | ![img](https://static.wixstatic.com/media/64c63b_d70a5a8102d14df6be57658f696ab28c~mv2.png/v1/fill/w_267,h_183,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_d70a5a8102d14df6be57658f696ab28c~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_36feb9bc9305402e8a9e044b7f42c06e~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_36feb9bc9305402e8a9e044b7f42c06e~mv2.png) |
| A36  | mouthShrugLower            | ![img](https://static.wixstatic.com/media/64c63b_c39b6573ab8b452c8ba9af4cfd61fa0d~mv2.png/v1/fill/w_267,h_183,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_c39b6573ab8b452c8ba9af4cfd61fa0d~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_881391abc1ff4fbabd6f7719d93179b8~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_881391abc1ff4fbabd6f7719d93179b8~mv2.png) |
| A37  | mouthClose                 | ![img](https://static.wixstatic.com/media/64c63b_7c1a9921e54c42c5bbad10ce2d2a2edc~mv2.png/v1/fill/w_267,h_129,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_7c1a9921e54c42c5bbad10ce2d2a2edc~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_8aded518da54400db938b69753b8539a~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_8aded518da54400db938b69753b8539a~mv2.png) |
| A38  | mouthSmileLeft             | ![img](https://static.wixstatic.com/media/64c63b_a3cdfd578cec40a5a83931c4d0c9f8ab~mv2.png/v1/fill/w_267,h_186,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_a3cdfd578cec40a5a83931c4d0c9f8ab~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_11aa5137231b4bfe8a8908f25d8d4112~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_11aa5137231b4bfe8a8908f25d8d4112~mv2.png) |
| A39  | mouthSmileRight            | ![img](https://static.wixstatic.com/media/64c63b_f0c7a9ddfcb945f496f4ac8aafcfd0ca~mv2.png/v1/fill/w_267,h_186,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_f0c7a9ddfcb945f496f4ac8aafcfd0ca~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_4818df7bf47740f6bab387d0d2926a2b~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_4818df7bf47740f6bab387d0d2926a2b~mv2.png) |
| A40  | mouthFrownLeft             | ![img](https://static.wixstatic.com/media/64c63b_8e7c89a5e9514206ac3fd7152e912ef8~mv2.png/v1/fill/w_267,h_187,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_8e7c89a5e9514206ac3fd7152e912ef8~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_ba5a9fdcf6d246439b8d7d9dbf63fb16~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_ba5a9fdcf6d246439b8d7d9dbf63fb16~mv2.png) |
| A41  | mouthFrownRight            | ![img](https://static.wixstatic.com/media/64c63b_019c769729a34c7c992c3bbde95adf2a~mv2.png/v1/fill/w_267,h_187,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_019c769729a34c7c992c3bbde95adf2a~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_4505259aa94646278b01cd6b4e6fe32a~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_4505259aa94646278b01cd6b4e6fe32a~mv2.png) |
| A42  | mouthDimpleLeft            | ![img](https://static.wixstatic.com/media/64c63b_b7c5c7b4fcea481ba877fab837ddda7c~mv2.png/v1/fill/w_267,h_187,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_b7c5c7b4fcea481ba877fab837ddda7c~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_53d010f6b8b340d6a305149152fe9eb2~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_53d010f6b8b340d6a305149152fe9eb2~mv2.png) |
| A43  | mouthDimpleRight           | ![img](https://static.wixstatic.com/media/64c63b_268dda3d9bb14eaba63c5b123ab9002c~mv2.png/v1/fill/w_267,h_187,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_268dda3d9bb14eaba63c5b123ab9002c~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_ea46553169c749f69dc8e47737434193~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_ea46553169c749f69dc8e47737434193~mv2.png) |
| A44  | mouthUpperUpLeft           | ![img](https://static.wixstatic.com/media/64c63b_e6f82a77cd374e37b456590eb19c2d28~mv2.png/v1/fill/w_267,h_186,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_e6f82a77cd374e37b456590eb19c2d28~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_5c9a52ea901243218e0c9252fcd45a00~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_5c9a52ea901243218e0c9252fcd45a00~mv2.png) |
| A45  | mouthUpperUpRight          | ![img](https://static.wixstatic.com/media/64c63b_384bab2c926045f99f4bbef75b6975f0~mv2.png/v1/fill/w_267,h_186,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_384bab2c926045f99f4bbef75b6975f0~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_8abd87f586bb4d2088673a2358a65adb~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_8abd87f586bb4d2088673a2358a65adb~mv2.png) |
| A46  | mouthLowerDownLeft         | ![img](https://static.wixstatic.com/media/64c63b_2511f8304fbb49dab88eb09b118f88bc~mv2.png/v1/fill/w_267,h_188,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_2511f8304fbb49dab88eb09b118f88bc~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_21506f6994114f1194bc69958bd3778d~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_21506f6994114f1194bc69958bd3778d~mv2.png) |
| A47  | mouthLowerDownRight        | ![img](https://static.wixstatic.com/media/64c63b_5c300e220ef04f388b827c096ad7aae6~mv2.png/v1/fill/w_267,h_188,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_5c300e220ef04f388b827c096ad7aae6~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_9ac53c48df9e4d63b6774b91aaa4db3d~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_9ac53c48df9e4d63b6774b91aaa4db3d~mv2.png) |
| A48  | mouthPressLeft             | ![img](https://static.wixstatic.com/media/64c63b_478c881ace1744ff825202484b212c17~mv2.png/v1/fill/w_267,h_187,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_478c881ace1744ff825202484b212c17~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_cca358e42c08454cb9f7f30317c4e93c~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_cca358e42c08454cb9f7f30317c4e93c~mv2.png) |
| A49  | mouthPressRight            | ![img](https://static.wixstatic.com/media/64c63b_acad007d32d24b26b4cc192345afc0ba~mv2.png/v1/fill/w_267,h_186,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_acad007d32d24b26b4cc192345afc0ba~mv2.png) | <br />![img](https://static.wixstatic.com/media/64c63b_35bac2e5acf54d438dd0acf4690c4ea2~mv2.png/v1/fill/w_230,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_35bac2e5acf54d438dd0acf4690c4ea2~mv2.png) |
| A50  | mouthStretchLeft           | ![img](https://static.wixstatic.com/media/64c63b_18fbf15030164a6383068c8fb7aa7e72~mv2.png/v1/fill/w_263,h_184,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_18fbf15030164a6383068c8fb7aa7e72~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_cf77104a546149e88698feb420726493~mv2.png/v1/fill/w_232,h_209,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_cf77104a546149e88698feb420726493~mv2.png) |
| A51  | mouthStretchRight          | ![img](https://static.wixstatic.com/media/64c63b_3f8dd987a3d44b7e98e1e7abb1815111~mv2.png/v1/fill/w_263,h_184,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_3f8dd987a3d44b7e98e1e7abb1815111~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_b2a3abb6ea204ab293571c7c19747003~mv2.png/v1/fill/w_232,h_209,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_b2a3abb6ea204ab293571c7c19747003~mv2.png) |
| A52  | tongueOut                  |                                                              | ![img](https://static.wixstatic.com/media/64c63b_10387f10b0e04d5fac672f8bd17d9459~mv2.png/v1/fill/w_232,h_209,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_10387f10b0e04d5fac672f8bd17d9459~mv2.png) |

- CC3 额外的舌头Blendshape(with open month)：

| T01  | Tongue_Up       |      | ![img](https://static.wixstatic.com/media/64c63b_75c512342cde45ffbb40fcf5d463732e~mv2.png/v1/fill/w_244,h_220,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_75c512342cde45ffbb40fcf5d463732e~mv2.png) |
| ---- | --------------- | ---- | ------------------------------------------------------------ |
| T02  | Tongue_Down     |      | ![img](https://static.wixstatic.com/media/64c63b_4bdf00b4d23d4a89ac0bffbb66cc348d~mv2.png/v1/fill/w_244,h_220,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_4bdf00b4d23d4a89ac0bffbb66cc348d~mv2.png) |
| T03  | Tongue_Left     |      | ![img](https://static.wixstatic.com/media/64c63b_860b7c7043894521a754755c35816cb3~mv2.png/v1/fill/w_244,h_220,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_860b7c7043894521a754755c35816cb3~mv2.png) |
| T04  | Tongue_Right    |      | ![img](https://static.wixstatic.com/media/64c63b_02c7adc74f934d31ad35c01615b96735~mv2.png/v1/fill/w_244,h_220,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_02c7adc74f934d31ad35c01615b96735~mv2.png) |
| T05  | Tongue_Roll     |      | ![img](https://static.wixstatic.com/media/64c63b_bfa27b0483c94f7484eeed246642fbc5~mv2.png/v1/fill/w_244,h_220,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_bfa27b0483c94f7484eeed246642fbc5~mv2.png) |
| T06  | Tongue_Tip_Up   |      | ![img](https://static.wixstatic.com/media/64c63b_6a7d96ce1444409c958adc03652983b7~mv2.png/v1/fill/w_244,h_220,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_6a7d96ce1444409c958adc03652983b7~mv2.png) |
| T07  | Tongue_Tip_Down |      | ![img](https://static.wixstatic.com/media/64c63b_37fa335ad1a549b983fb6552db3b5198~mv2.png/v1/fill/w_244,h_220,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_37fa335ad1a549b983fb6552db3b5198~mv2.png) |

### Vive面部的表情基准组

Vive这一套脸部追踪也是52个blendshapes，但是和苹果的基准有很大区别。

- 区别一：舌头

苹果其实是52+7，因为舌头在52个里只有一个伸舌头的blendshape，但vive其实是42 + 10，整体来讲Vive表情记住能tracking到的表情细节还是更少一些。

- 区别二：眉毛

ARKit的52个blendshapes，是根据硬件分区一对一tracking的，然而Vive眉毛不分是没有单独另设blendshapes，而是与眼睛的动作blended在一起作为一个blendshape的，并不是精准的一对一分区tracking。

我下面编号的排序是按照[VIVE Eye and Facial Tracking SDK](https://developer.vive.com/resources/vive-sense/sdk/vive-eye-and-facial-tracking-sdk/) unity 里inspector里的顺序，方便我加表情。

这里是整理的用ARKit制作Vive基准的对应编号：

[https://docs.google.com/spreadsheets/d/1kWXnqtiVbXRb1FrD5NLlxxuxbYmS0Z6YBLuIE1WwqD4/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1kWXnqtiVbXRb1FrD5NLlxxuxbYmS0Z6YBLuIE1WwqD4/edit?usp=sharing)

- Eye Blendshapes （14 = 12 + 2）

| Vive编号 | Vive表情基准                                                 | Vive Picture                                                 | Create by CC3 blendshapes                                    |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| V01      | Eye_Left_Blink                                               | ![img](https://static.wixstatic.com/media/64c63b_735cb0ae227e42bca98f9c51fbd0df6b~mv2.png/v1/fill/w_238,h_182,al_c,lg_1,q_85,enc_auto/64c63b_735cb0ae227e42bca98f9c51fbd0df6b~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_e5f3c0dfc63a42618e182a9b1a0c1e9c~mv2.png/v1/fill/w_211,h_188,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_e5f3c0dfc63a42618e182a9b1a0c1e9c~mv2.png) |
| V02      | Eye_Left_Wide                                                | ![img](https://static.wixstatic.com/media/64c63b_1d9223fb44574a94988a7c9ce4d89b39~mv2.png/v1/fill/w_222,h_160,al_c,lg_1,q_85,enc_auto/64c63b_1d9223fb44574a94988a7c9ce4d89b39~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_5dd9ed05165f4fe9b486b4f0604dacc1~mv2.png/v1/fill/w_211,h_188,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_5dd9ed05165f4fe9b486b4f0604dacc1~mv2.png) |
| V03      | Eye_Left_Right                                               | ![img](https://static.wixstatic.com/media/64c63b_638f42e4960743c4b235ab18b5ac6eba~mv2.png/v1/fill/w_238,h_188,al_c,lg_1,q_85,enc_auto/64c63b_638f42e4960743c4b235ab18b5ac6eba~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_c5fcda96b7184941b2a89b2193470f2b~mv2.png/v1/fill/w_211,h_188,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_c5fcda96b7184941b2a89b2193470f2b~mv2.png) |
| V04      | Eye_Left_Left                                                | ![img](https://static.wixstatic.com/media/64c63b_a1041585f54748728dd71aec7de129f5~mv2.png/v1/fill/w_238,h_192,al_c,lg_1,q_85,enc_auto/64c63b_a1041585f54748728dd71aec7de129f5~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_a26c36f7dc2940fe9513e263f7a99c4e~mv2.png/v1/fill/w_211,h_188,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_a26c36f7dc2940fe9513e263f7a99c4e~mv2.png) |
| V05      | Eye_Left_Up                                                  | ![img](https://static.wixstatic.com/media/64c63b_d2c84d05015c4d8289f6c7d6d5ba0dcc~mv2.png/v1/fill/w_238,h_203,al_c,lg_1,q_85,enc_auto/64c63b_d2c84d05015c4d8289f6c7d6d5ba0dcc~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_e3e67e16e4b84697a39c3333bad24712~mv2.png/v1/fill/w_211,h_188,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_e3e67e16e4b84697a39c3333bad24712~mv2.png) |
| V06      | Eye_Left_Down                                                | ![img](https://static.wixstatic.com/media/64c63b_5cd43316383549e282e7f3f743df9053~mv2.png/v1/fill/w_238,h_195,al_c,lg_1,q_85,enc_auto/64c63b_5cd43316383549e282e7f3f743df9053~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_993bd278fb024580a834a71c6886cc4b~mv2.png/v1/fill/w_211,h_188,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_993bd278fb024580a834a71c6886cc4b~mv2.png) |
| V07      | Eye_Right_Blink                                              | ![img](https://static.wixstatic.com/media/64c63b_2e198e55d97a491cbc66059e6f6adddc~mv2.png/v1/fill/w_235,h_195,al_c,lg_1,q_85,enc_auto/64c63b_2e198e55d97a491cbc66059e6f6adddc~mv2.png) |                                                              |
| V08      | Eye_Right_Wide                                               | ![img](https://static.wixstatic.com/media/64c63b_6eebbecf575d4bec905be4dbec06322c~mv2.png/v1/fill/w_223,h_160,al_c,lg_1,q_85,enc_auto/64c63b_6eebbecf575d4bec905be4dbec06322c~mv2.png) |                                                              |
| V09      | Eye_Right_Right                                              | ![img](https://static.wixstatic.com/media/64c63b_fc88e475e8c4435a98364224f54ade1a~mv2.png/v1/fill/w_234,h_197,al_c,lg_1,q_85,enc_auto/64c63b_fc88e475e8c4435a98364224f54ade1a~mv2.png) |                                                              |
| V10      | Eye_Right_Left                                               | ![img](https://static.wixstatic.com/media/64c63b_216b900672314c37a3e91501b7fe7cc1~mv2.png/v1/fill/w_238,h_190,al_c,lg_1,q_85,enc_auto/64c63b_216b900672314c37a3e91501b7fe7cc1~mv2.png) |                                                              |
| V11      | Eye_Right_Up                                                 | ![img](https://static.wixstatic.com/media/64c63b_062847a5c45d4dabbe78d255779013dd~mv2.png/v1/fill/w_231,h_196,al_c,lg_1,q_85,enc_auto/64c63b_062847a5c45d4dabbe78d255779013dd~mv2.png) |                                                              |
| V12      | Eye_Right_Down                                               | ![img](https://static.wixstatic.com/media/64c63b_b6fae35fba8543d0becc535532111d23~mv2.png/v1/fill/w_238,h_176,al_c,lg_1,q_85,enc_auto/64c63b_b6fae35fba8543d0becc535532111d23~mv2.png) |                                                              |
| V13      | Eye_Left_squeeze: The blendShape close eye tightly when Eye_Left_Blink  value is 100. | ![img](https://static.wixstatic.com/media/64c63b_c7b07f1b4ec6495685d85808d23c04e8~mv2.png/v1/fill/w_238,h_183,al_c,lg_1,q_85,enc_auto/64c63b_c7b07f1b4ec6495685d85808d23c04e8~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_a629d31ace624dd8b2ded5123123156e~mv2.png/v1/fill/w_211,h_188,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_a629d31ace624dd8b2ded5123123156e~mv2.png) |
| V14      | Eye_Right_squeeze                                            | ![img](https://static.wixstatic.com/media/64c63b_b82c535f90874742b3c0b6ff62136fe2~mv2.png/v1/fill/w_238,h_194,al_c,lg_1,q_85,enc_auto/64c63b_b82c535f90874742b3c0b6ff62136fe2~mv2.png) |                                                              |

- Lip Blendshapes （38 = 37 + 1）

| Vive编号 | Vive表情基准            | Vive Picture                                                 | Create by CC3 blendshapes                                    |
| -------- | ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| V15      | Jaw_Right               | ![img](https://static.wixstatic.com/media/64c63b_75f8b68a96104ef8bf36e393c7ecd48b~mv2.png/v1/fill/w_235,h_190,al_c,lg_1,q_85,enc_auto/64c63b_75f8b68a96104ef8bf36e393c7ecd48b~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_65471d28b0d743c0bb6232ffaee0f6b6~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_65471d28b0d743c0bb6232ffaee0f6b6~mv2.png) |
| V16      | Jaw_Left                | ![img](https://static.wixstatic.com/media/64c63b_9cacde29288c4523a2192835a736ad6b~mv2.png/v1/fill/w_245,h_202,al_c,lg_1,q_85,enc_auto/64c63b_9cacde29288c4523a2192835a736ad6b~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_017d7142fd494aef9ad7bbe53fa1d6eb~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_017d7142fd494aef9ad7bbe53fa1d6eb~mv2.png) |
| V17      | Jaw_Forward             | ![img](https://static.wixstatic.com/media/64c63b_3876f3dd1a1b4eed92e8405b42700190~mv2.png/v1/fill/w_248,h_197,al_c,lg_1,q_85,enc_auto/64c63b_3876f3dd1a1b4eed92e8405b42700190~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_20353f83579541428557c32d92545c9e~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_20353f83579541428557c32d92545c9e~mv2.png) |
| V18      | Jaw_Open                | ![img](https://static.wixstatic.com/media/64c63b_dc79f10003534839948d3261183d5082~mv2.png/v1/fill/w_244,h_188,al_c,lg_1,q_85,enc_auto/64c63b_dc79f10003534839948d3261183d5082~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_24470b9cc9964a11906c42b1d1a6e5e9~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_24470b9cc9964a11906c42b1d1a6e5e9~mv2.png) |
| V19      | Mouth_Ape_Shape         | ![img](https://static.wixstatic.com/media/64c63b_7a0f9461a760449db12b2159009ccc93~mv2.png/v1/fill/w_249,h_196,al_c,lg_1,q_85,enc_auto/64c63b_7a0f9461a760449db12b2159009ccc93~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_3d7911f5bfa645adb7f3c36fbeafa2b9~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_3d7911f5bfa645adb7f3c36fbeafa2b9~mv2.png) |
| V20      | Mouth_Upper_Right       | ![img](https://static.wixstatic.com/media/64c63b_01037e0042754059b7ada72a8adf2e8a~mv2.png/v1/fill/w_227,h_161,al_c,lg_1,q_85,enc_auto/64c63b_01037e0042754059b7ada72a8adf2e8a~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_185ec305ba464016a15c2420fb04916e~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_185ec305ba464016a15c2420fb04916e~mv2.png) |
| V21      | Mouth_Upper_Left        | ![img](https://static.wixstatic.com/media/64c63b_f0c61e8f3f3c42d7ad6d83703f1a61d9~mv2.png/v1/fill/w_265,h_182,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_f0c61e8f3f3c42d7ad6d83703f1a61d9~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_abbecb4860a44fe9800585825beb4b17~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_abbecb4860a44fe9800585825beb4b17~mv2.png) |
| V22      | Mouth_Lower_Right       | ![img](https://static.wixstatic.com/media/64c63b_3ec74984b19d44d389a68bcc1ac1a7fb~mv2.png/v1/fill/w_265,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_3ec74984b19d44d389a68bcc1ac1a7fb~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_80a4cdffa3fb493e9c153b517d9aebda~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_80a4cdffa3fb493e9c153b517d9aebda~mv2.png) |
| V23      | Mouth_Lower_Left        | ![img](https://static.wixstatic.com/media/64c63b_e80cee8738ea42528c8f351303f5e2c8~mv2.png/v1/fill/w_265,h_225,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_e80cee8738ea42528c8f351303f5e2c8~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_edf8e441ff994c27bde811a21754d5e5~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_edf8e441ff994c27bde811a21754d5e5~mv2.png) |
| V24      | *Mouth_Upper_Overturn   | ![img](https://static.wixstatic.com/media/64c63b_5f77c14164ae48cf9c0cf4c762b97837~mv2.png/v1/fill/w_265,h_202,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_5f77c14164ae48cf9c0cf4c762b97837~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_b8ae358e723f42e199338722f186e238~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_b8ae358e723f42e199338722f186e238~mv2.png) |
| V25      | *Mouth_Lower_Overturn   | ![img](https://static.wixstatic.com/media/64c63b_16a26f9ced50420b99a4c32fc296c112~mv2.png/v1/fill/w_265,h_210,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_16a26f9ced50420b99a4c32fc296c112~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_282323813dfa4ea1aa76551b112e3919~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_282323813dfa4ea1aa76551b112e3919~mv2.png) |
| V26      | Mouth_Pout              | ![img](https://static.wixstatic.com/media/64c63b_e7da853fe63242a9bedbd7fe3bddadc7~mv2.png/v1/fill/w_265,h_205,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_e7da853fe63242a9bedbd7fe3bddadc7~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_36615908f74d4663a6bc438c3287938c~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_36615908f74d4663a6bc438c3287938c~mv2.png) |
| V27      | Mouth_Smile_Right       | ![img](https://static.wixstatic.com/media/64c63b_1de129dc23784dd0af8d5bbccff75741~mv2.png/v1/fill/w_265,h_205,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_1de129dc23784dd0af8d5bbccff75741~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_47a00d3e749e47fa8b3489da81252654~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_47a00d3e749e47fa8b3489da81252654~mv2.png) |
| V28      | Mouth_Smile_Left        | ![img](https://static.wixstatic.com/media/64c63b_e66c5606123d4272bc4d3206a101e884~mv2.png/v1/fill/w_265,h_213,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_e66c5606123d4272bc4d3206a101e884~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_0a26740959644351bb01f9e9d40ef35e~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_0a26740959644351bb01f9e9d40ef35e~mv2.png) |
| V29      | Mouth_Sad_Right         | ![img](https://static.wixstatic.com/media/64c63b_ba5427a221c2446e9d3b9e30d94d80b9~mv2.png/v1/fill/w_265,h_224,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_ba5427a221c2446e9d3b9e30d94d80b9~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_c1e99be3d6c34038852ce55b72102f5c~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_c1e99be3d6c34038852ce55b72102f5c~mv2.png) |
| V30      | Mouth_Sad_Left          | ![img](https://static.wixstatic.com/media/64c63b_00772c50ca334cbf95dd1bf53be4c6b8~mv2.png/v1/fill/w_265,h_218,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_00772c50ca334cbf95dd1bf53be4c6b8~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_889e2637303f4d7195afd699a3d92b86~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_889e2637303f4d7195afd699a3d92b86~mv2.png) |
| V31      | Cheek_Puff_Right        | ![img](https://static.wixstatic.com/media/64c63b_765350d6685547d4b03b7ae31e7346e0~mv2.png/v1/fill/w_265,h_224,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_765350d6685547d4b03b7ae31e7346e0~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_66386b8d632b4556a00f886613f26d92~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_66386b8d632b4556a00f886613f26d92~mv2.png) |
| V32      | Cheek_Puff_Left         | ![img](https://static.wixstatic.com/media/64c63b_2998211eb141496d8651b786337b7846~mv2.png/v1/fill/w_265,h_213,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_2998211eb141496d8651b786337b7846~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_833f433253fb4bcc8e380d79120b3003~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_833f433253fb4bcc8e380d79120b3003~mv2.png) |
| V33      | Cheek_Suck              | ![img](https://static.wixstatic.com/media/64c63b_6eea541e05494d26a06cbbe5377cdc0a~mv2.png/v1/fill/w_265,h_209,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_6eea541e05494d26a06cbbe5377cdc0a~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_8573de7fc0d84245a0fa4412ecd3e842~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_8573de7fc0d84245a0fa4412ecd3e842~mv2.png) |
| V34      | Mouth_Upper_UpRight     | ![img](https://static.wixstatic.com/media/64c63b_b6ca87cbb7774b2ab4f0ec3748ec9c51~mv2.png/v1/fill/w_265,h_216,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_b6ca87cbb7774b2ab4f0ec3748ec9c51~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_c48b985609fe4129ad1dac8a41905a7e~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_c48b985609fe4129ad1dac8a41905a7e~mv2.png) |
| V35      | Mouth_Upper_ UpLeft     | ![img](https://static.wixstatic.com/media/64c63b_58bdc8db0ac3451388534ff3bfb0fa83~mv2.png/v1/fill/w_265,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_58bdc8db0ac3451388534ff3bfb0fa83~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_5ff3f05aeecd48fe9f3077f5c9c96569~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_5ff3f05aeecd48fe9f3077f5c9c96569~mv2.png) |
| V36      | Mouth_Lower_DownRight   | ![img](https://static.wixstatic.com/media/64c63b_12f26efe2f28425cb366eea55e83470c~mv2.png/v1/fill/w_265,h_223,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_12f26efe2f28425cb366eea55e83470c~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_30ae27fa9ee94aa8a1b29bbd5fe7b0b2~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_30ae27fa9ee94aa8a1b29bbd5fe7b0b2~mv2.png) |
| V37      | Mouth_Lower_DownLeft    | ![img](https://static.wixstatic.com/media/64c63b_4ed1a27945324b53aad0aa3cf453a275~mv2.png/v1/fill/w_265,h_218,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_4ed1a27945324b53aad0aa3cf453a275~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_76893f9855fa4a5a9415cd8abfae6f6f~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_76893f9855fa4a5a9415cd8abfae6f6f~mv2.png) |
| V38      | Mouth_Upper_Inside      | ![img](https://static.wixstatic.com/media/64c63b_f5e050f0d9954760879ccd18185c2fc8~mv2.png/v1/fill/w_265,h_209,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_f5e050f0d9954760879ccd18185c2fc8~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_5217c686c7c6455aaca6ba1b2ce64217~mv2.png/v1/fill/w_224,h_200,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_5217c686c7c6455aaca6ba1b2ce64217~mv2.png) |
| V39      | Mouth_Lower_Inside      | ![img](https://static.wixstatic.com/media/64c63b_0031f9adda4441cbb6361e280e594c7b~mv2.png/v1/fill/w_269,h_211,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_0031f9adda4441cbb6361e280e594c7b~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_5108178f718e492eb840f4d678eb3e4e~mv2.png/v1/fill/w_217,h_193,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_5108178f718e492eb840f4d678eb3e4e~mv2.png) |
| V40      | Mouth_Lower_Overlay     | ![img](https://static.wixstatic.com/media/64c63b_26e5bd6286474b4ea3f4fff3933b91f1~mv2.png/v1/fill/w_269,h_222,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_26e5bd6286474b4ea3f4fff3933b91f1~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_1ab252df4c5146e1815e23a83edb2cd2~mv2.png/v1/fill/w_217,h_193,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_1ab252df4c5146e1815e23a83edb2cd2~mv2.png) |
| V41      | Tongue_LongStep1        | ![img](https://static.wixstatic.com/media/64c63b_6791ccfceffe4c2ca07f277b91037521~mv2.png/v1/fill/w_269,h_207,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_6791ccfceffe4c2ca07f277b91037521~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_4ef4ab94e1ef47dcb01facf5d168f1d1~mv2.png/v1/fill/w_217,h_193,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_4ef4ab94e1ef47dcb01facf5d168f1d1~mv2.png) |
| V42      | Tongue_LongStep2        | ![img](https://static.wixstatic.com/media/64c63b_e79ccc0096a54ce2b48d188cf6907d0c~mv2.png/v1/fill/w_269,h_181,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_e79ccc0096a54ce2b48d188cf6907d0c~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_6e560524670843848266701061f24c63~mv2.png/v1/fill/w_217,h_193,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_6e560524670843848266701061f24c63~mv2.png) |
| V43      | *Tongue_Down            | ![img](https://static.wixstatic.com/media/64c63b_ac97c6cf9fd940e9b38cdf22ab3c9261~mv2.png/v1/fill/w_269,h_199,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_ac97c6cf9fd940e9b38cdf22ab3c9261~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_a2a8aab70eea4b6ba9378cf249aef3a0~mv2.png/v1/fill/w_217,h_193,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_a2a8aab70eea4b6ba9378cf249aef3a0~mv2.png) |
| V44      | *Tongue_Up              | ![img](https://static.wixstatic.com/media/64c63b_0c11f06c560842718309c52bc159ffa8~mv2.png/v1/fill/w_269,h_197,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_0c11f06c560842718309c52bc159ffa8~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_0abc5fe7b2da4c988591e18fc6e060ac~mv2.png/v1/fill/w_217,h_193,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_0abc5fe7b2da4c988591e18fc6e060ac~mv2.png) |
| V45      | *Tongue_Right           | ![img](https://static.wixstatic.com/media/64c63b_0d6e1976f6c342a395f9631be529c694~mv2.png/v1/fill/w_269,h_202,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_0d6e1976f6c342a395f9631be529c694~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_e17db94c36594f32b60ce6057a17aafc~mv2.png/v1/fill/w_217,h_193,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_e17db94c36594f32b60ce6057a17aafc~mv2.png) |
| V46      | *Tongue_Left            | ![img](https://static.wixstatic.com/media/64c63b_2633b9481a6f4e94ad4bfe6a6d52e122~mv2.png/v1/fill/w_269,h_201,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_2633b9481a6f4e94ad4bfe6a6d52e122~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_ad949214aeda4b3488c238af7aabdba6~mv2.png/v1/fill/w_217,h_193,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_ad949214aeda4b3488c238af7aabdba6~mv2.png) |
| V47      | *Tongue_Roll            | ![img](https://static.wixstatic.com/media/64c63b_4d41918f9af84d0aaaa2de1e354a5706~mv2.png/v1/fill/w_269,h_216,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_4d41918f9af84d0aaaa2de1e354a5706~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_2c544b45c0ea48079bb570912b85b2a3~mv2.png/v1/fill/w_217,h_193,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_2c544b45c0ea48079bb570912b85b2a3~mv2.png) |
| V48      | *Tongue_UpLeft_Morph    | ![img](https://static.wixstatic.com/media/64c63b_49d65415de0f47d5a07aa77cfebd54e6~mv2.png/v1/fill/w_269,h_201,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_49d65415de0f47d5a07aa77cfebd54e6~mv2.png) ![img](https://static.wixstatic.com/media/64c63b_9df53a0e560f41f2a441f9e799b56d1c~mv2.png/v1/fill/w_269,h_221,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_9df53a0e560f41f2a441f9e799b56d1c~mv2.png) |                                                              |
| V49      | *Tongue_UpRight_Morph   | ![img](https://static.wixstatic.com/media/64c63b_118b5229d2274b5f95a163ebc0d0cfad~mv2.png/v1/fill/w_269,h_232,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_118b5229d2274b5f95a163ebc0d0cfad~mv2.png) ![img](https://static.wixstatic.com/media/64c63b_aa40430e533c40c69f0addb2df019a29~mv2.png/v1/fill/w_269,h_215,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_aa40430e533c40c69f0addb2df019a29~mv2.png) |                                                              |
| V50      | *Tongue_DownLeft_Morph  | ![img](https://static.wixstatic.com/media/64c63b_92fc463c5efc4436a23870d596023ba9~mv2.png/v1/fill/w_269,h_237,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_92fc463c5efc4436a23870d596023ba9~mv2.png) ![img](https://static.wixstatic.com/media/64c63b_b3a74eba5433479b96ff645e85681480~mv2.png/v1/fill/w_269,h_231,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_b3a74eba5433479b96ff645e85681480~mv2.png) |                                                              |
| V51      | *Tongue_DownRight_Morph | ![img](https://static.wixstatic.com/media/64c63b_db25fb8a736e4b1f9f4e11ba7436e0b0~mv2.png/v1/fill/w_269,h_224,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_db25fb8a736e4b1f9f4e11ba7436e0b0~mv2.png) ![img](https://static.wixstatic.com/media/64c63b_b707961c295f40a7995644e93e438ffc~mv2.png/v1/fill/w_269,h_212,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_b707961c295f40a7995644e93e438ffc~mv2.png) |                                                              |
| V52      | *O-shaped mouth         | ![img](https://static.wixstatic.com/media/64c63b_97cacb52babe4a109cd02874efcb2eda~mv2.png/v1/fill/w_269,h_175,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_97cacb52babe4a109cd02874efcb2eda~mv2.png) | ![img](https://static.wixstatic.com/media/64c63b_6e98ff0232d349b8a6f7d8348992ab37~mv2.png/v1/fill/w_217,h_193,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_6e98ff0232d349b8a6f7d8348992ab37~mv2.png) ![img](https://static.wixstatic.com/media/64c63b_b35e7f3707fc4b0ca75f80c4d77867a4~mv2.png/v1/fill/w_217,h_193,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/64c63b_b35e7f3707fc4b0ca75f80c4d77867a4~mv2.png) |

## MediaPipe提取BlendShape

MediaPipe Face Landmarker解决方案最初于5月的Google I/O 2023发布。它可以检测面部landmark并输出blendshape score，以渲染与用户匹配的3D面部模型。通过MediaPipe Face Landmarker解决方案，KDDI和谷歌成功地为虚拟主播带来了真实感。

**技术实现**

使用Mediapipe强大而高效的Python包，KDDI开发人员能够检测表演者的面部特征并实时提取52个混合形状。

还可参考：[https://colab.research.google.com/github/googlesamples/mediapipe/blob/main/examples/face_landmarker/python/%5BMediaPipe_Python_Tasks%5D_Face_Landmarker.ipynb](https://colab.research.google.com/github/googlesamples/mediapipe/blob/main/examples/face_landmarker/python/%5BMediaPipe_Python_Tasks%5D_Face_Landmarker.ipynb)

```python
import mediapipe as mp
from mediapipe.tasks import python as mp_python
import time

MP_TASK_FILE = "face_landmarker_with_blendshapes.task"

class FaceMeshDetector:
    def __init__(self):
        with open(MP_TASK_FILE, mode="rb") as f:
            f_buffer = f.read()
        
        # 创建配置选项
        base_options = mp_python.BaseOptions(model_asset_buffer=f_buffer)
        options = mp_python.vision.FaceLandmarkerOptions(
            base_options=base_options,
            output_face_blendshapes=True,
            output_facial_transformation_matrixes=True,
            running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
            num_faces=1,
            result_callback=self.mp_callback
        )
        
        # 创建模型
        self.model = mp_python.vision.FaceLandmarker.create_from_options(options)
        self.landmarks = None
        self.blendshapes = None
        self.latest_time_ms = 0

    def mp_callback(self, mp_result, output_image, timestamp_ms: int):
        # 处理回调结果
        if len(mp_result.face_landmarks) >= 1 and len(mp_result.face_blendshapes) >= 1:
            self.landmarks = mp_result.face_landmarks[0]
            self.blendshapes = [b.score for b in mp_result.face_blendshapes[0]]

    def update(self, frame):
        t_ms = int(time.time() * 1000)
        if t_ms <= self.latest_time_ms:
            return
        
        frame_mp = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        self.model.detect_async(frame_mp, t_ms)
        self.latest_time_ms = t_ms

    def get_results(self):
        return self.landmarks, self.blendshapes
```



## 参考

- [https://www.mianzi-lizi.com/post/blendshape学习笔记](https://www.mianzi-lizi.com/post/blendshape学习笔记)
- [利用Animoji技术识别用户的表情](https://www.toutiao.com/article/6915330866285691395/)
- [通过MediaPipe解决方案来为虚拟主播带来更逼真真实感](https://news.nweon.com/110210)
- [Unity & FACEGOOD Audio2Face 通过音频驱动面部BlendShape](https://bbs.huaweicloud.com/blogs/374337)
- [GenerativeAI Avatar solutions](https://www.cnblogs.com/jesse123/p/9014234.html)