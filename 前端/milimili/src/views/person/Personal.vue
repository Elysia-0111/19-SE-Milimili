<template>
  <div class="personal">

    <div class="PersonTop">
      <div class="PersonTop_img">
        <img :src="this.avatar" @click="editavatar" />
        <input type="file" ref="fileInput" style="display: none;" @change="uploadAvatar">
      </div>
      <div class="PersonTop_text">
        <div class="user_text">
          <div class="user_name">
            <span> {{ this.nickname }} </span>
          </div>
          <!-- <div class="user-v">
            <img src="@/assets/logo.png" class="user-v-img" />
            <span class="user-v-font">大会员</span>
          </div> -->
          <!-- <div class="user_qianming">
            <span> user_qianming </span>
          </div> -->
          <div v-if="this.id != this.input">

          </div>
          <div v-else>
            <div class="user_anniu">
              <el-button class="el-icon-edit" type="primary" size="medium" @click="editnickname">编辑昵称</el-button>
            </div>
          </div>
        </div>
        <el-col :span="14"></el-col>
        <div class="user_num">
          <div style="cursor: pointer" @click="myfan">
            <div class="num_number">{{ this.fannum }}</div>
            <span class="num_text">粉丝</span>
          </div>
          <div style="cursor: pointer" @click="myfollow">
            <div class="num_number">{{ this.follownum }}</div>
            <span class="num_text">关注</span>
          </div>
          <div>
            <div class="num_number">{{ this.likenum }}</div>
            <span class="num_text">获赞</span>
          </div>
        </div>
      </div>
    </div>
    <div class="person_body">
      <div class="person_body_left">
        <el-card class="box-card" :body-style="{ padding: '0px' }">
          <div slot="header" class="clearfix">
            <span class="person_body_list" style="border-bottom: none">个人中心</span>
          </div>
          <!-- <div
              class="person_body_list"
              v-for="(item, index) in person_body_list"
              :key="index"
            >
              <router-link :to="{ name: item.name, params: item.params }">{{
                item.label
              }}</router-link>
            </div> -->
          <el-menu router active-text-color="#00c3ff" class="el-menu-vertical-demo">

            <el-menu-item index="myarticle" :route="{ name: 'myarticle' }">
              <i class="el-icon-edit-outline"></i>
              <span slot="title">上传视频</span>
            </el-menu-item>
            <el-menu-item index="mycollect" :route="{ name: 'mycollect' }">
              <i class="el-icon-document"></i>
              <span slot="title">收藏</span>
            </el-menu-item>
            <el-menu-item index="myfan" :route="{ name: 'myfan', query: { userid: input } }">
              <i class="el-icon-tableware"></i>
              <span slot="title">粉丝</span>
            </el-menu-item>
            <el-menu-item index="myfollow" :route="{ name: 'myfollow', query: { userid: input } }">
              <i class="el-icon-circle-plus-outline"></i>
              <span slot="title">关注</span>
            </el-menu-item>
            <div v-if="this.id != this.input">
              <div v-if="followuser.includes(this.input)">
                <el-menu-item @click="unfollow(this.input)">
                  <i class="el-icon-user"></i>
                  <span slot="title">取消关注</span>
                </el-menu-item>
              </div>
              <div v-else>
                <el-menu-item @click="follow(this.input)">
                  <i class="el-icon-user"></i>
                  <span slot="title">关注用户</span>
                </el-menu-item>
              </div>
            </div>
            <div v-else>
              <el-menu-item @click="editsignature">
                <i class="el-icon-user"></i>
                <span slot="title">修改个性签名</span>
              </el-menu-item>
            </div>

          </el-menu>
        </el-card>
      </div>
      <div class="person_body_right">
        <a>{{ this.signature }}</a>
      </div>
    </div>
  </div>
  <el-backtop></el-backtop>
</template>
  

    

<script>
import axios from "axios";
import PersonalDia from "./PersonalDia.vue";

export default {
  components: { PersonalDia },
  name: "Personal",
  inject: ["reload"],
  data() {
    return {
      id: 0,
      avatar: "",
      nickname: "",
      v: 1,
      design: "",
      follownum: 0,
      fannum: 0,
      likenum: 0,
      isfollow: true,
      followData: {
        fanId: "",
        followId: "",
      },
      isfollowid: [],
      input: 0,
      signature: "",
      followuser: [],
      FormData: new FormData()
    };
  },
  mounted() {
    this.input = parseInt(window.location.search.substring(8))

    this.FormData.append("user_id", this.input)
    axios.post('http://127.0.0.1:8000/api/show/', this.FormData).then(res => {
      this.avatar = res.data.user.avatar_url
      this.nickname = res.data.user.nickname
      this.fannum = res.data.user.fan_num
      // console.log(this.fannum)
      this.likenum = res.data.user.like_num
      // console.log(this.likenum)
      this.follownum = res.data.user.follow_num
      this.signature = res.data.user.signature

    })
    axios.get('http://127.0.0.1:8000/api/get_userid/').then(res => {
      // this.nickname = res.data.user.nickname
      // this.fannum = res.data.user.fan_num
      // // console.log(this.fannum)
      // this.likenum = res.data.user.like_num
      // // console.log(this.likenum)
      // this.follownum = res.data.user.follow_num
      // this.signature = res.data.user.signature
      this.id = res.data.result
      console.log(this.id)
    }),



      console.log(this.input)
  },
  watch: {
    $route() {
      //this.$emit("flesh");
    },
  },
  methods: {
    edit() {
    },
    editnickname() {
      this.$prompt('请输入昵称', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(({ value }) => {
        // this.$message({
        //   type: 'success',
        //   message: '你的邮箱是: ' + value
        // });
        this.nickname = value
        let data = new FormData()
        data.append("nickname", this.nickname)
        data.append("signature", this.signature)
        axios.post('http://127.0.0.1:8000/api/change_file/', data)
          .then(res => {
            alert(res.data.message)
          })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消输入'
        });
      });

    },
    editsignature() {
      this.$prompt('请输入个性签名', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(({ value }) => {
        // this.$message({
        //   type: 'success',
        //   message: '你的邮箱是: ' + value
        // });
        this.signature = value
        let data = new FormData()
        data.append("nickname", this.nickname)
        data.append("signature", this.signature)
        axios.post('http://127.0.0.1:8000/api/change_file/', data)
          .then(res => {
            alert(res.data.message)
          })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消输入'
        });
      });

    },
    editavatar() {
      this.$refs.fileInput.click()
    },
    uploadAvatar() {
      const file = this.$refs.fileInput.files[0];
      const data = new FormData();
      data.append("avatar", file)
      axios.post('http://127.0.0.1:8000/api/upload_avatar/', data)
        .then(res => {
          alert(res.data.message)
        })
    },
    follow(id) {
      let data = new FormData();
      data.append("follow_id", id)
      axios.post('http://127.0.0.1:8000/api/follow/', data).then(res => {
        if (res.data.result == 2) {
          alert(res.data.message)
          return
        }
        alert(res.data.message)
        location.reload()
      })


    },
    unfollow(id) {
      let data = new FormData();
      data.append("follow_id", id)
      axios.post('http://127.0.0.1:8000/api/unfollow/', data).then(res => {
        alert(res.data.message)
        location.reload()
      })

    },

  }, created() {
    axios.get('http://127.0.0.1:8000/api/havefollow/').then(res => {
      if (res.data.result != 0) {
        this.followuser = res.data.follow_list
      }

      console.log(1)
      console.log(this.followuser)


    })
  }
};
</script>
<style>
dq {
  width: 100%;
  height: 100%;
  background-color: #c8c8c8;
}

.header2 {
  width: auto;
  height: 75px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  background-color: rgb(255, 255, 255);
}

.linkhead {
  text-decoration: none;
  color: wheat;
  font-size: large;
}

a {
  text-decoration: none;
  color: black;
}

.fonthead {
  color: rgb(0, 0, 0);
  font-size: large;
}

.img1 {
  transform: translateY(-30%);
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

.PersonTop {
  width: 1000px;
  height: 140px;
  padding-top: 20px;
  background-color: rgb(255, 255, 255);
  margin-top: 30px;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  border-radius: 5px rgba(0, 0, 0, 0.1);
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.PersonTop_img {
  width: 150px;
  height: 120px;
  background-color: #8c939d;
  margin-right: 24px;
  margin-left: 20px;
  overflow: hidden;
  border-radius: 20px;
}

.PersonTop_img img {
  width: 100%;
  height: 100%;
  border-radius: 20px;
}

.PersonTop_text {
  height: 120px;
  width: 880px;
  display: flex;
}

.user_text {
  width: 20%;
  height: 100%;
  line-height: 30px;
}

.user_name {
  font-weight: bold;
}

.user_name span {
  font-size: 20px;
}

.user_anniu {
  margin-top: 30%;
}

.user-v {
  margin-bottom: -5px;
}

.user-v-img {
  width: 15px;
  height: 15px;
}

.user-v-font {
  font-size: 15px;
  color: #00c3ff;
}

.user_qianming {
  font-size: 14px;
  color: #999;
}

.user_num {
  width: 80%;
  height: 100%;
  display: flex;
  align-items: center;
}

.user_num>div {
  text-align: center;
  border-right: 1px dotted #999;
  box-sizing: border-box;
  width: 80px;
  height: 40px;
  line-height: 20px;
}

.num_text {
  color: #999;
}

.num_number {
  font-size: 20px;
  color: #333;
}

.el-menu-item>span {
  font-size: 16px;
  color: #999;
}

/*下面部分样式*/
.person_body {
  width: 1000px;
  margin-top: 210px;
  display: flex;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 5px;
}

.person_body_left {
  width: 27%;
  height: 480px;
  border-radius: 5px;
  margin-right: 3%;
  text-align: center;
}

.person_body_list {
  width: 100%;
  height: 50px;
  margin-top: 25px;
  font-size: 22px;
  border-bottom: 1px solid #f0f0f0;
  background-image: -webkit-linear-gradient(left,
      rgb(42, 134, 141),
      #e9e625dc 20%,
      #3498db 40%,
      #e74c3c 60%,
      #09ff009a 80%,
      rgba(82, 196, 204, 0.281) 100%);
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  -webkit-background-size: 200% 100%;
  -webkit-animation: masked-animation 4s linear infinite;
}

.el-menu-item {
  margin-top: 22px;
}

.person_body_right {
  width: 70%;
  /* height: 500px; */
  border-radius: 5px;
  background-color: white;
}

.person_body_right a {
  font-size: 70px;
  font-family: STXingkai;

}

.box-card {
  height: 500px;
}

/*ui样式*/
.el-button {
  width: 84px;
}
</style>
  