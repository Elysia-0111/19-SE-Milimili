<template>
    <div class="userclass">
        <div v-if="isDefault" :user="defaultUsers">
            <div class="userclass-grid">
                <div v-for="user in user" class="user-container">
                    <div class="user-grid">
                        <div class="avatar-container">
                            <div class="avatar-inner">
                                <img class="avatar" v-bind:src="user.avatar">
                            </div>
                        </div>
                        <div class="user-container">
                            <div class="user-container-grid">
                                <div class="username">
                                    <a class="usernamefond" :href="gethref(user.id)">{{ user.nickname }}</a>
                                </div>
                                <div class="userinformation">
                                    <a>{{ formatNumber(user.fan_num) }}粉丝</a>
                                    <a> &#8226 </a>
                                    <a>{{ user.video_num }}个视频</a>
                                </div>
                                <div v-if="followuser.includes(user.id)">
                                    <div class="followbutton">
                                        <el-button class="followbutton" type="info" icon="Minus" size="large"
                                            @click="unfollow(user.id)">取消关注</el-button>
                                    </div>
                                </div>
                                <div v-else>
                                    <div class="followbutton">
                                        <el-button class="followbutton" type="primary" icon="Plus" size="large"
                                            @click="follow(user.id)">关注用户</el-button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="isDown" :user="downsortedUsers">
            <div class="userclass-grid">
                <div v-for="user in user" class="user-container">
                    <div class="user-grid">
                        <div class="avatar-container">
                            <div class="avatar-inner">
                                <img class="avatar" v-bind:src="user.avatar">
                            </div>
                        </div>
                        <div class="user-container">
                            <div class="user-container-grid">
                                <div class="username">
                                    <a class="usernamefond" href="">{{ user.nickname }}</a>
                                </div>
                                <div class="userinformation">
                                    <a>{{ formatNumber(user.fan_num) }}粉丝</a>
                                    <a> &#8226 </a>
                                    <a>{{ user.video_num }}个视频</a>
                                </div>
                                <div v-if="followuser.includes(user.id)">
                                    <div class="followbutton">
                                        <el-button class="followbutton" type="info" icon="Minus" size="large"
                                            @click="unfollow(user.id)">取消关注</el-button>
                                    </div>
                                </div>
                                <div v-else>
                                    <div class="followbutton">
                                        <el-button class="followbutton" type="primary" icon="Plus" size="large"
                                            @click="follow(user.id)">关注用户</el-button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="isUp" :user="upsortedUsers">
            <div class="userclass-grid">
                <div v-for="user in user" class="user-container">
                    <div class="user-grid">
                        <div class="avatar-container">
                            <div class="avatar-inner">
                                <img class="avatar" v-bind:src="user.avatar">
                            </div>
                        </div>
                        <div class="user-container">
                            <div class="user-container-grid">
                                <div class="username">
                                    <a class="usernamefond" href="">{{ user.nickname }}</a>
                                </div>
                                <div class="userinformation">
                                    <a>{{ formatNumber(user.fan_num) }}粉丝</a>
                                    <a> &#8226 </a>
                                    <a>{{ user.video_num }}个视频</a>
                                </div>
                                <div v-if="followuser.includes(user.id)">
                                    <div class="followbutton">
                                        <el-button class="followbutton" type="info" icon="Minus" size="large"
                                            @click="unfollow(user.id)">取消关注</el-button>
                                    </div>
                                </div>
                                <div v-else>
                                    <div class="followbutton">
                                        <el-button class="followbutton" type="primary" icon="Plus" size="large"
                                            @click="follow(user.id)">关注用户</el-button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style>
.userclass {
    margin-left: 4%;
    margin-right: 4%;
}

.userclass-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-auto-rows: 150px;

}

.user-grid {
    display: grid;
    grid-template-columns: 1fr 4fr;
    column-gap: 1%;
}

.user-container-grid {
    display: grid;
    grid-template-rows: 12fr 9fr 16fr;

}

.avatar-inner {
    height: 93px;
    width: 93px;
    transform: translateY(10%);
}

.avatar-inner img {
    width: 100%;
    height: 100%;
    object-fit: fill;
    border-radius: 50%;
}

.username {
    text-align: left;
}



.usernamefond {
    text-decoration: none;
    color: black;
    font-weight: bold;
    font-size: 30px;
}

.usernamefond:hover {
    color: deepskyblue;
}

.userinformation {
    text-align: left;
}

.userinformation a {
    color: #909399;
}

.followbutton {
    display: flex;
    align-items: center;
}
</style>
<script>
import axios from 'axios';
import { mapState } from 'vuex';


export default {

    data() {
        return {
            users: [
                {
                    id: 'user1',
                    name: 'xyz',
                    avatar: require('../../../assets/头像.jpg'),
                    fan: 1,
                    video: 2
                },
                {
                    id: 'user4',
                    name: 'test',
                    avatar: require('../../../assets/头像.jpg'),
                    fan: 23423430,
                    video: 20
                },
                {
                    id: 'user2',
                    name: 'abc',
                    avatar: require('../../../assets/头像.jpg'),
                    fan: 1023000,
                    video: 20
                },
                {
                    id: 'user3',
                    name: 'abc',
                    avatar: require('../../../assets/头像.jpg'),
                    fan: 11230,
                    video: 20
                },

            ],
            user: [],
            followuser: [],
        }
    },
    methods: {
        formatNumber(number) {
            if (number > 10000) {
                return (number / 10000).toFixed(1) + "万";
            } else {
                return number.toString();
            }
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
        gethref: function (id) {
            return '/personal?userid=' + id;

        }



    },
    computed: {
        defaultUsers() {
            return this.user.sort((a, b) => a.nickname.localeCompare(b.nickname))
        },
        upsortedUsers() {
            return this.user.sort((a, b) => a.fan_num - b.fan_num)
        },
        downsortedUsers() {
            return this.user.sort((a, b) => b.fan_num - a.fan_num)
        },
        isDefault() {
            const prefix = '/search/user/default';
            return this.$route.path.startsWith(prefix);
        },
        isDown() {
            const prefix = '/search/user/down';
            return this.$route.path.startsWith(prefix);
        },
        isUp() {
            const prefix = '/search/user/up';
            return this.$route.path.startsWith(prefix);
        },
        ...mapState['searchinput'],


    },
    mounted() {
        console.log(window.location.search.substring(7))
        let data = new FormData();
        data.append("type", 'user')
        data.append("query", window.location.search.substring(7))
        // console.log(data)
        console.log(this.user)
        axios.post('http://127.0.0.1:8000/api/search/', data)
            .then(res => {
                // for (var pair of res.data.user.entries()) {
                //     this.user.push(pair)
                // }

                console.log(res.data.user)
                this.user = res.data.user
                console.log(this.user)

            })
    },
    created() {
        axios.get('http://127.0.0.1:8000/api/havefollow/').then(res => {
            if (res.data.result != 0) {
                this.followuser = res.data.follow_list
            }

            console.log(1)
            console.log(this.followuser)
        })
    }
}
</script>