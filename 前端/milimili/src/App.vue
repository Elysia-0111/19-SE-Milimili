<template>
  <el-container>
    <el-header>
      <div v-if="this.$store.state.isLogin == false">
        <router-link to="/video/home">VideoHome</router-link> |
        <router-link to="/home">Home</router-link> |
        <!--<router-link to="/homepage">个人中心</router-link> |-->
        <router-link to="/personal/">主页界面</router-link> |
        <router-link to="/about">About</router-link> |
        <router-link to="/login">登录</router-link> |
        <router-link to="/register">注册</router-link>
      </div>
      <div v-else>
        <router-link to="/video/1">VideoView</router-link> |
        <router-link to="/home">VideoHome</router-link> |
        <router-link to="/">Home</router-link> |
        <!--<router-link :to="{ name: 'personal', params:this.$store.state.id }">个人中心</router-link> |-->
        <router-link :to="{name: 'personal', params: { id: this.$store.state.id }}">主页界面</router-link> |
        <router-link to="/about">About</router-link> |
        <el-button type="info" @click="this.$store.commit('logout')">退出登录</el-button>
      </div>
    </el-header>
  </el-container>
  <router-view />
</template>

<script>
export default{
  mounted() {
  },
  methods: {
    saveState() {
      this.$store.commit("saveToken", this.$storage._session.get('id'));
    },
  },
}
</script>

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
