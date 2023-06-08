<template>
    <div class="login">
        <div v-if="this.$store.state.isLogin == false">
            <div class="container">
                <div class="main">
                    <!-- 整个注册盒子 -->
                    <div class="loginbox">
                        <!-- 左侧的注册盒子 -->
                        <div class="loginbox-in">
                            <div class="userbox">
                                <el-avatar :size="30"> user </el-avatar>
                                <input v-model="username" class="user" id="user" placeholder="用户名">
                            </div>
                            <br>
                            <div class="pwdbox">
                                <el-avatar :size="30"> pwd </el-avatar>
                                <input v-model="password" class="pwd" id="password" type="password" placeholder="密码">
                            </div>
                            <br>
                            <el-button type="primary" @click="loginUser">登录</el-button> |
                            <router-link to="/register"><el-button class="register_btn"
                                    type="success">注册</el-button></router-link>
                        </div>
                        <!-- 右侧的注册盒子 -->
                        <div class="background">
                            <div class="title">Welcome to MiLiMiLi</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-else>
            <el-button type="info" @click="this.$store.commit('logout')">退出登录</el-button>
        </div>
    </div>
</template>
<style>
.loginbox {
    display: flex;
    position: absolute;
    width: 800px;
    height: 400px;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 12px 16px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 #4E655D;
}

.loginbox-in {
    background-color: #89AB9E;
    width: 240px;
}

.userbox {
    margin-top: 120px;
    height: 30px;
    width: 230px;
    display: flex;
    margin-left: 25px;
}

.pwdbox {
    height: 30px;
    width: 225px;
    display: flex;
    margin-left: 25px;
}

.title {
    margin-top: 320px;
    font-weight: bold;
    font-size: 20px;
    color: #4E655D;

}

.title:hover {
    font-size: 21px;
    transition: all 0.4s ease-in-out;
    cursor: pointer;
}

.uesr-text {
    position: left;
}

input:focus {
    border-bottom: 2px solid #445b53;
    background-color: transparent;
    transition: all 0.2s ease-in;
    font-family: sans-serif;
    font-size: 15px;
    color: #445b53;
    font-weight: bold;

}

input:hover {
    border-bottom: 2px solid #445b53;
    background-color: transparent;
    transition: all 0.2s ease-in;
    font-family: sans-serif;
    font-size: 15px;
    color: #445b53;
    font-weight: bold;

}

input:-webkit-autofill {
    /* 修改默认背景框的颜色 */
    box-shadow: 0 0 0px 1000px #89AB9E inset !important;
    /* 修改默认字体的颜色 */
    -webkit-text-fill-color: #445b53;
}

input:-webkit-autofill::first-line {
    /* 修改默认字体的大小 */
    font-size: 15px;
    /* 修改默认字体的样式 */
    font-weight: bold;
}

.log-box {
    font-size: 12px;
    display: flex;
    justify-content: space-between;
    width: 190px;
    margin-left: 30px;
    color: #4E655D;
    margin-top: -5px;
    align-items: center;

}

.log-box {
    font-size: 12px;
    display: flex;
    justify-content: space-between;
    width: 190px;
    margin-left: 30px;
    color: #4E655D;
    margin-top: -5px;
    align-items: center;

}

.log-box-text {
    color: #4E655D;
    font-size: 12px;
    text-decoration: underline;
}

.login_btn {
    background-color: #5f8276;
    /* Green */
    border: none;
    color: #FAFAFA;
    padding: 5px 22px;
    text-align: center;
    text-decoration: none;
    font-size: 13px;
    border-radius: 20px;
    outline: none;
}

.login_btn:hover {
    box-shadow: 0 12px 16px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 rgba(0, 0, 0, 0.19);
    cursor: pointer;
    background-color: #0b5137;
    transition: all 0.2s ease-in;
}

.warn {
    margin-top: 60px;
    /* margin-right:120px; */
    margin-left: -120px;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 17px;
}

.background {
    width: 570px;
    background-image: url('../assets/login.jpg');
    background-size: cover;
    font-family: sans-serif;
}
</style>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        loginUser() {
            if (this.username == '') {
                alert("请输入用户名")
                return
            }
            if (this.password == '') {
                alert("请输入密码");
                return
            }

            let data = new FormData();
            data.append("username", this.username)
            data.append("password", this.password)
            axios.post('http://127.0.0.1:8000/api/login/', data)
                .then(response => {
                    // 注册成功后的处理逻辑
                    this.$message.success("登录成功，3秒后进入主页");
                    const timejump = 3;
                    if (!this.timer) {
                        this.count = timejump;
                        this.show = false;
                        this.timer = setInterval(() => {
                            if (this.count > 0 && this.count <= timejump) {
                                this.count--;
                            } else {
                                this.show = true;
                                clearInterval(this.timer);
                                this.timer = null;
                                //跳转的页面写在此处
                                this.$router.push({ path: '/home' });
                            }
                        }, 1000)
                    }
                })
                .catch(error => {
                    console.error('Registration failed', error);
                    alert("登录失败，请重新")
                });

        }
    }
}
</script>
