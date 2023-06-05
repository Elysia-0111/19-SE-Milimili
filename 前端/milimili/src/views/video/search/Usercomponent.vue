<template>
    <div class="userclass">
        <div v-if="isDefault" :user="defaultUsers">
            <div class="userclass-grid">
                <div v-for="user in users" class="user-container">
                    <div class="user-grid">
                        <div class="avatar-container">
                            <div class="avatar-inner">
                                <img class="avatar" v-bind:src="user.avatar">
                            </div>
                        </div>
                        <div class="user-container">
                            <div class="user-container-grid">
                                <div class="username">
                                    <a class="usernamefond" href="">{{ user.name }}</a>
                                </div>
                                <div class="userinformation">
                                    <a>{{ formatNumber(user.fan) }}粉丝</a>
                                    <a> &#8226 </a>
                                    <a>{{ user.video }}个视频</a>
                                </div>
                                <div class="followbutton">
                                    <el-button class="followbutton" type="primary" icon="Plus" size="large">关注</el-button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="isDown" :user="downsortedUsers">
            <div class="userclass-grid">
                <div v-for="user in users" class="user-container">
                    <div class="user-grid">
                        <div class="avatar-container">
                            <div class="avatar-inner">
                                <img class="avatar" v-bind:src="user.avatar">
                            </div>
                        </div>
                        <div class="user-container">
                            <div class="user-container-grid">
                                <div class="username">
                                    <a class="usernamefond" href="">{{ user.name }}</a>
                                </div>
                                <div class="userinformation">
                                    <a>{{ formatNumber(user.fan) }}粉丝</a>
                                    <a> &#8226 </a>
                                    <a>{{ user.video }}个视频</a>
                                </div>
                                <div class="followbutton">
                                    <el-button class="followbutton" type="primary" icon="Plus" size="large">关注</el-button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="isUp" :user="upsortedUsers">
            <div class="userclass-grid">
                <div v-for="user in users" class="user-container">
                    <div class="user-grid">
                        <div class="avatar-container">
                            <div class="avatar-inner">
                                <img class="avatar" v-bind:src="user.avatar">
                            </div>
                        </div>
                        <div class="user-container">
                            <div class="user-container-grid">
                                <div class="username">
                                    <a class="usernamefond" href="">{{ user.name }}</a>
                                </div>
                                <div class="userinformation">
                                    <a>{{ formatNumber(user.fan) }}粉丝</a>
                                    <a> &#8226 </a>
                                    <a>{{ user.video }}个视频</a>
                                </div>
                                <div class="followbutton">
                                    <el-button class="followbutton" type="primary" icon="Plus" size="large">关注</el-button>
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

            ]
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
    },
    computed: {
        defaultUsers() {
            return this.users.sort((a, b) => a.id.localeCompare(b.id))
        },
        upsortedUsers() {
            return this.users.sort((a, b) => a.fan - b.fan)
        },
        downsortedUsers() {
            return this.users.sort((a, b) => b.fan - a.fan)
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
        }
    }
}
</script>