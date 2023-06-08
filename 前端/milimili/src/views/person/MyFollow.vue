<template>
  <div class="fanorfollow_box">
    <div v-if="this.userlist != null">

      <div v-for="user in userlist">
        <div class="fanorfollow">
          <div class="fanorfollow_left">
            <img class="fanorfollow_img" src="@/assets/logo.png" />
          </div>
          <div class="fanorfollow_info">
            <div class="fanorfollow_info_top">
              <span style="color: #666; max-width: 180px">{{ user.nickname }}</span>
            </div>
            <div class="fanorfollow_info_bottom">
              <span>123</span>
            </div>
          </div>
          <div class="fanorfollow_botton">
            <el-button type="primary" size="small" round icon="el-icon-check" v-text="'取消关注'"
              @click="unfollow(user.id)"></el-button>
          </div>
        </div>
      </div>
    </div>

    <div v-else>
      <div>
        <el-empty :image-size="250" description="这里什么都没有哟"></el-empty>
      </div>

    </div>
  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  name: "MyFanAndFollow",
  inject: ["reload"],
  data() {
    return {
      userlist: []
    };
  },
  mounted() {
    let data = new FormData()
    data.append("user_id", window.location.search.substring(8))
    axios.post('http://127.0.0.1:8000/api/getfollow/', data)
      .then(res => {

        if (res.data.result == -1) {
          this.userlist = null
        } else {
          this.userlist = res.data.user
        }
        console.log(this.userlist)
      })
  },
  methods: {
    unfollow(id) {
      let data = new FormData();
      data.append("follow_id", id)
      axios.post('http://127.0.0.1:8000/api/unfollow/', data).then(res => {
        alert(res.data.message)
        location.reload()
      })
    }
  }

}

</script>
  
<style>
.fanorfollow_box :hover {
  border-width: 1px;
  border-color: deepskyblue;
}

.fanorfollow {
  padding: 15px 40px 15px 30px;
  height: 50px;
  display: flex;
  align-items: center;
  border: 1px solid #ebebeb;
}

.fanorfollow :hover {
  border-width: 1px;
  border-color: deepskyblue;
}

.fanorfollow_left {
  width: 60px;
  height: 60px;
}

.fanorfollow_img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  border: 1px solid #ebebeb;
  vertical-align: top;
}

.fanorfollow_info {
  display: inline-block;
  margin-left: 20px;
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  overflow: hidden;
}

.fanorfollow_info_top {
  display: inline-block;
  font-size: 10;
  line-height: 14px;
  vertical-align: top;
  cursor: pointer;
}

.fanorfollow_info_top :hover {
  color: deepskyblue;
}

.fanorfollow_info_bottom {
  line-height: 14px;
  color: #999;
  margin-top: 5px;
  cursor: pointer;
}

.fanorfollow_info_bottom :hover {
  color: deepskyblue;
}
</style>
  