<template>
  <el-container>
    <el-header>

      <div v-if="this.isLogin">
        <router-link to="/video/1">VideoView</router-link> |
        <router-link to="/home">VideoHome</router-link> |
        <router-link to="/">Home</router-link> |
        <!--<router-link to="/homepage">个人中心</router-link> |-->
        <router-link to="/personal">主页界面</router-link> |
        <router-link to="/about">About</router-link> |
        <el-button type="info" @click="logout">退出登录</el-button>

      </div>
      <div v-else>
        <router-link to="/video/home">VideoHome</router-link> |
        <router-link to="/">Home</router-link> |
        <!--<router-link to="/homepage">个人中心</router-link> |-->
        <router-link to="/personal">主页界面</router-link> |
        <router-link to="/about">About</router-link> |
        <router-link to="/login">登录</router-link> |
        <router-link to="/register">注册</router-link>
      </div>
    </el-header>
  </el-container>
  <router-view />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
<script>
import { computed } from 'vue'

export default {
  data() {
    return {
      isLogin: sessionStorage.getItem('isLogin')
    }
  },
  methods: {
    logout() {
      sessionStorage.removeItem('isLogin')
      this.isLogin = 'false'
      location.reload()
      console.log(sessionStorage.getItem('isLogin'))
    }
  },




}

</script>
