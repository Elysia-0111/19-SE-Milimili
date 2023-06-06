<template>
  <div class="personal">
    <el-container>
      <el-header class="header2">
        <el-row>
          <el-col :span="1" :offset="1"><router-link class="linkhead" to="../../video/home"><a
                class="fonthead">首页</a></router-link></el-col>
          <el-col :span="1" class="fonthead"><router-link to="../../video/home"><a
                class="fonthead">热门</a></router-link></el-col>
          <el-col :span="1" class="fonthead"><router-link to="../../video/home"><a
                class="fonthead">频道</a></router-link></el-col>
          <el-col :span="6" :offset="3">
            <el-input v-model="searchinput" size="small" placeholder="Please input">
              <template #append>
                <el-button type="primary" icon="Search" circle></el-button>
              </template>
            </el-input>
          </el-col>
          <el-col :span="3" :offset="3"><router-link to="/personal">
              <img class="img1" src="../../assets/img/V.png">
            </router-link>
          </el-col>
          <el-col :span="1"><router-link to="../../personal">
              <el-icon size="24">
                <ChatLineSquare />
              </el-icon>
            </router-link>
          </el-col>
          <el-col :span="1"><router-link to="../../personal/mycollect">
              <el-icon size="24">
                <Collection />
              </el-icon>
            </router-link>
          </el-col>
          <el-col :span="1"><router-link to="../../home">
              <el-icon size="24">
                <VideoPlay />
              </el-icon>
            </router-link>
          </el-col>


          <el-col :span="1"><router-link to="../../personal/upload">
              <el-icon size="24">
                <Upload />
              </el-icon>
            </router-link>
          </el-col>
        </el-row>
      </el-header>
    </el-container>
    <div class="PersonTop">
      <div class="PersonTop_img">
        <img src="@/assets/img/V.png" />
      </div>
      <div class="PersonTop_text">
        <div class="user_text">
          <div class="user_name">
            <span> {{ nickname }} </span>
          </div>
          <div class="user-v" v-if="v === 3">
            <img src="@/assets/logo.png" class="user-v-img" />
            <span class="user-v-font">大会员</span>
          </div>
          <div class="user_qianming">
            <span> {{ design }} </span>
          </div>
          <div class="user_anniu">
            <el-button
              class="el-icon-edit"
              v-if="this.$route.params.id === this.$store.state.id"
              type="primary"
              size="medium"
              plain
              @click="edit"
              >编辑</el-button
            >
            <!--<router-link to="../../personal/personaldia"><el-button class="el-icon-edit" type="primary"
                size="medium">编辑</el-button></router-link>-->
          </div>
        </div>
        <el-col :span="14"></el-col>
        <div class="user_num">
          <div style="cursor: pointer" @click="myfan">
            <div class="num_number"> {{ fanCounts }} </div>
            <span class="num_text">粉丝</span>
          </div>
          <div style="cursor: pointer" @click="myfollow">
            <div class="num_number"> {{ followCounts }} </div>
            <span class="num_text">关注</span>
          </div>
          <div>
            <div class="num_number"> {{ goodCounts }} </div>
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
            <!--
          <el-menu router active-text-color="#00c3ff" class="el-menu-vertical-demo">
            <el-menu-item index="info" :route="{ name: 'info' }">
              <i class="el-icon-user"></i>
              <span slot="title">个人简介</span>
            </el-menu-item>
            <el-menu-item index="myarticle" :route="{ name: 'myarticle' }">
              <i class="el-icon-edit-outline"></i>
              <span slot="title">上传视频</span>
            </el-menu-item>
            <el-menu-item index="mycollect" :route="{ name: 'mycollect' }">
              <i class="el-icon-document"></i>
              <span slot="title">收藏</span>
            </el-menu-item>
            <el-menu-item index="myfan" :route="{ name: 'myfan' }">
              <i class="el-icon-tableware"></i>
              <span slot="title">粉丝</span>
            </el-menu-item>
            <el-menu-item index="myfollow" :route="{ name: 'myfollow' }">
              <i class="el-icon-circle-plus-outline"></i>
              <span slot="title">关注</span>
            </el-menu-item>
          </el-menu>-->
          <el-menu
            router
            active-text-color="#00c3ff"
            class="el-menu-vertical-demo"
          >
            <el-menu-item
              index="info"
              :route="{ name: 'info'}"
            >
              <i class="el-icon-user"></i>
              <span slot="title">个人简介</span>
            </el-menu-item>
            <el-menu-item
              index="myarticle"
              :route="{ name: 'myarticle'}"
            >
              <i class="el-icon-edit-outline"></i>
              <span slot="title">发帖</span>
            </el-menu-item>
            <el-menu-item
              index="mycollect"
              :route="{ name: 'mycollect'}"
            >
              <i class="el-icon-document"></i>
              <span slot="title">收藏</span>
            </el-menu-item>
            <el-menu-item
              index="myfan"
              :route="{ name: 'myfan'}"
            >
              <i class="el-icon-tableware"></i>
              <span slot="title">粉丝</span>
            </el-menu-item>
            <el-menu-item
              index="myfollow"
              :route="{ name: 'myfollow'}"
            >
              <i class="el-icon-circle-plus-outline"></i>
              <span slot="title">关注</span>
            </el-menu-item>
          </el-menu>
        </el-card>
      </div>
      <div class="person_body_right">
        <router-view></router-view>
      </div>
    </div>
    <div v-if="x === 1"><personal-dia ref="dia" @flesh="reload" /></div>
  </div>
  <el-backtop></el-backtop>
</template>
  

    

<script>
import PersonalDia from "./PersonalDia.vue";

export default {
  components: { PersonalDia },
  name: "Personal",
  inject: ["reload"],
  data() {
    return {
      avatar: "",
      nickname: "lulu",
      v: 1,
      x:0,
      design: "这里是个性签名",
      followCounts: "5",
      fanCounts: "7",
      goodCounts: "11",
      isfollow: true,
      followData: {
        fanId: "",
        followId: "",
      },
      isfollowid: [],
    };
  },
  mounted() {
    this.load();
  },
  watch: {
    $route(to, from) {
        
    },
  },
  methods: {
    load() {

    },
    edit() {
      this.$router.push({ path: `/personal/personaldia` })
    },
    toInfo(){
      this.$router.push({ path: `/personal/info` })
    },
    toMyArticle(){
      this.$router.push({path:`/personal/myarticle`})
    },
    toMyCollect(){
      this.$router.push({path:`/personal/mycollect`})
    }
  },
};
</script>

<style scoped>
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
  height: 600px;
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

.box-card {
  height: 500px;
}

/*ui样式*/
.el-button {
  width: 84px;
}
</style>
  