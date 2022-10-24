![alt text](https://github.com/KaydeeJR/logistics-optimization-causal-inference/blob/Main/causal_inference.png)

<h1 align="center">Welcome to Location Optimization using Causal Inference 👋</h1>
<p>
</p>

> This project contains code that visualizes driver locations. Performs causal inference to determine the cause behind incomplete deliveries.

## Install


Clone the project

```bash
git clone https://github.com/KaydeeJR/logistics-optimization-causal-inference
```
Install dependencies

```sh
pip3 install -r requirements.txt
```
## Directory Structure

```
logistics-optimization-causal-inference
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ ORIG_HEAD
│  ├─ branches
│  ├─ config
│  ├─ description
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ Main
│  │     └─ remotes
│  │        └─ origin
│  │           ├─ HEAD
│  │           └─ Main
│  ├─ objects
│  │  ├─ 00
│  │  │  └─ bc345a54f2f046809d80f4bac10509d4c63ad1
│  │  ├─ 03
│  │  │  └─ cfdbc88ac028f91731d1e3e1a01645e59e35df
│  │  ├─ 04
│  │  │  └─ 6dd759c19349a3f873c184dd68f1578dedaee4
│  │  ├─ 0a
│  │  │  └─ 912c96b1abc65b780ad4d797dff502ce3e6f99
│  │  ├─ 0e
│  │  │  └─ 19418f399b1dd77cb1ae16a71eea64c7c5a718
│  │  ├─ 10
│  │  │  └─ e9357c8d1436c99d0b67a8bb1f7ad21b3bbc14
│  │  ├─ 16
│  │  │  └─ 8141cea23aadcbc909a99bf3b4a1cc56a1589a
│  │  ├─ 1a
│  │  │  ├─ 0138ce80467fcc7d62151c1fa96075f89ec121
│  │  │  └─ bc6aaea453ec0bef785a00d57bcfba52779e21
│  │  ├─ 20
│  │  │  └─ d300f098482086649c989628c3764f75f9e979
│  │  ├─ 32
│  │  │  └─ 89163bcb461a6f436f7ad28e3576aad51a9e67
│  │  ├─ 33
│  │  │  └─ 6457403fb96e0c3242a9115462e41f578f3457
│  │  ├─ 36
│  │  │  └─ 5e4be05478bcaad83d5279b14f05683354bb69
│  │  ├─ 37
│  │  │  └─ da7d6db6b3c11ded464191b84559c3061cc7b7
│  │  ├─ 3e
│  │  │  └─ bc1d7b151057ceafc4be7cfaeaa2d8680a4a4e
│  │  ├─ 44
│  │  │  └─ 6c26e37ff4fb343b6fb08dca7be176a2083f60
│  │  ├─ 46
│  │  │  └─ 6b8b185a15495f3e4d3c40f09eb714036d826b
│  │  ├─ 4e
│  │  │  └─ 5bba20c17769877a7f7ac2a8d7799083f6482a
│  │  ├─ 4f
│  │  │  └─ 0e2fe1e85db358475800ad3df44a3b8cf3c9af
│  │  ├─ 51
│  │  │  └─ 973055237895f2d23e65e015793fd302f4b9da
│  │  ├─ 52
│  │  │  └─ 8f30c71c687de473bbb506c071e902beba6cd9
│  │  ├─ 56
│  │  │  └─ c5d4b62ddcc88f121b257e1b9b5b69b1e4c6c2
│  │  ├─ 59
│  │  │  └─ 5013b6fe71dce3ca505b2d3e0ecf4429769a32
│  │  ├─ 67
│  │  │  ├─ 0c7e310c70863473ab1336ca79908b09f99710
│  │  │  └─ 9b0676d57e169d2ba9e91ab47959d89c16e668
│  │  ├─ 6a
│  │  │  └─ f53205f71d1da9fa990071a33ec372a32c1e7e
│  │  ├─ 77
│  │  │  └─ 72691dd7fa1ce1dc77df874a9504bd11c7de69
│  │  ├─ 80
│  │  │  └─ e1fc86cfbe51ddb822ceba68d1e3bf28b83577
│  │  ├─ 82
│  │  │  └─ 63dc2cfca0db5b4f0c997782b82e3ad2346e55
│  │  ├─ 83
│  │  │  └─ 2436d55caf503686ecf0e2bad95d0495b68a20
│  │  ├─ 85
│  │  │  └─ 1ef1a6cbb479169f4884b108a52471fe98fa17
│  │  ├─ 87
│  │  │  └─ d42204c6472a42e146a50b4f769e37646cba21
│  │  ├─ 8a
│  │  │  └─ 675f9d0e6222f07020ed1e3bcf78971f8d0918
│  │  ├─ 8b
│  │  │  └─ 137891791fe96927ad78e64b0aad7bded08bdc
│  │  ├─ 8e
│  │  │  └─ 53cd38af6509a0fb531bbebdf5b0a7e0a54b39
│  │  ├─ 8f
│  │  │  └─ aa52748c81545ded4825e578a0e32fb660c7ee
│  │  ├─ 94
│  │  │  └─ 0c8da49d5d5dad94a83ace0460ffe9982f9f38
│  │  ├─ 95
│  │  │  ├─ 47a021f46190f879b2bc44996dfb262fbd7104
│  │  │  └─ b90a756ca0899000558922ebacf8ae720db80c
│  │  ├─ 96
│  │  │  └─ c70e2515990ba5caf1ca0cfddfd1fa4bd5b1d5
│  │  ├─ 97
│  │  │  └─ 3bd4a36c603ac9ed2835b6d231738e24a4bb17
│  │  ├─ 9c
│  │  │  └─ 04d6a5543991582a637e832999838589619cd6
│  │  ├─ 9e
│  │  │  └─ 508e0f795a40bce7699c6b5aadfe7c45e7ebbf
│  │  ├─ a0
│  │  │  └─ 335f09406b9cc7ede0eecd37e6be0469aedfdb
│  │  ├─ a5
│  │  │  └─ 002a7b118411ffa2a1b8ee18d11df82b0a3429
│  │  ├─ a8
│  │  │  └─ b45acdbc9da98ae305ce6adebb5beb5bd71fbe
│  │  ├─ ac
│  │  │  └─ e602f7e36c8a529b1e539ef18346ad9e3a3002
│  │  ├─ ae
│  │  │  └─ 524a02c6f5127c15df7298b4590fc456d925e8
│  │  ├─ bd
│  │  │  └─ be0aaaca2633c072f23b1df395651d3f1423fd
│  │  ├─ c4
│  │  │  └─ a0e78de469eeacb7d2ab44fe22eb9172b70839
│  │  ├─ c5
│  │  │  └─ 5906b48c8345509ef637786d6df0d9d2399454
│  │  ├─ c9
│  │  │  ├─ 40d44642531845a6533d35e3d81ee1a7298b51
│  │  │  └─ f706829d3c2602ce625d9bc6d8c9b560ca477e
│  │  ├─ cb
│  │  │  └─ 46f46d777f083d6a86e2e8de44e6c05ff5435d
│  │  ├─ cd
│  │  │  └─ 76fa93206b07ac587cccc041874c857326b8b8
│  │  ├─ ce
│  │  │  └─ a6e5b35dca2803d0f04724f86d593c3013749f
│  │  ├─ d3
│  │  │  ├─ 5725218cf40112cb3b9baa1cccdc815bf9aed6
│  │  │  └─ 7929128aa8e46c737a443c15e5b693ac6d74cf
│  │  ├─ d8
│  │  │  └─ fc50121ab4a8155953a437f5c2f4ca37b67f10
│  │  ├─ d9
│  │  │  └─ f9e80667133c8fa2272d2e42c55c0a7e51b04f
│  │  ├─ de
│  │  │  └─ d07cf02b26d12a0eabefafea3a0a68321ac680
│  │  ├─ e0
│  │  │  └─ a8bf6509fea33cd8c0ef81cfc1d4b9a06af65a
│  │  ├─ e6
│  │  │  └─ 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│  │  ├─ eb
│  │  │  └─ a1a5a168acc75e870b2fa3524b89bc335de4f4
│  │  ├─ ed
│  │  │  └─ 131440f7d4c1337f602405847a0602cd9bed0b
│  │  ├─ f1
│  │  │  ├─ a62032fc58b4f4dcd8c834661834302b941db0
│  │  │  └─ c10e2c63a8434b9fb82d99ea6df46eab4e46bc
│  │  ├─ f6
│  │  │  └─ 0dfc9bb7cfa10a682dfe3b649e5cdc60a589c2
│  │  ├─ f7
│  │  │  └─ fc05ac23bd9e9dd47e1996147c57ac2c1c284b
│  │  ├─ f8
│  │  │  └─ ffac95a134ae4b228002f78419b32c18b8a9cb
│  │  ├─ f9
│  │  │  ├─ 8a91efc57edcf6523cb4be804730b4bf3b1009
│  │  │  └─ ee5259f595afde985a23bcc76d13342eddd9f1
│  │  ├─ fa
│  │  │  └─ 9c6bced702c47e1dc0b86f27d7dcd305c88e71
│  │  ├─ fd
│  │  │  └─ fa6213fe981ad7bb75f590d3df809b2cafd21a
│  │  ├─ fe
│  │  │  └─ 716230e46e509c463c9c6ffae96942bac6ee59
│  │  ├─ ff
│  │  │  └─ 8510af19b91ec61395975e831ce88af29b209e
│  │  ├─ info
│  │  └─ pack
│  │     ├─ pack-2f5f0e3aced2966583e554c6a66a60c88540fc09.idx
│  │     └─ pack-2f5f0e3aced2966583e554c6a66a60c88540fc09.pack
│  ├─ packed-refs
│  └─ refs
│     ├─ heads
│     │  └─ Main
│     ├─ remotes
│     │  └─ origin
│     │     ├─ HEAD
│     │     └─ Main
│     └─ tags
│        ├─ v1.0-dloc
│        ├─ v1.0-merged
│        └─ v1.0-nb
├─ .github
│  └─ workflows
│     └─ XGBoostCML.yaml
├─ .gitignore
├─ .vscode
│  └─ settings.json
├─ LICENSE
├─ README.md
├─ models
│  └─ dummy.txt
├─ notebooks
│  ├─ gokada_eda.ipynb
│  └─ gokada_merged_eda.ipynb
├─ screenshots
│  ├─ DVC_file_tracking.png
│  ├─ DVC_file_tracking_merged.png
│  └─ driver_locations.png
├─ scripts
│  ├─ __pycache__
│  │  └─ access_drive_file.cpython-310.pyc
│  ├─ add_to_sql.py
│  ├─ dloc_schema.sql
│  └─ nb_schema.sql
└─ tests
   └─ dummy.txt

```

## Author

👤 **Janerose Nyambura Njogu**


## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
