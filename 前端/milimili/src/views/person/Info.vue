<template>
  <div>
    <el-card>
      <el-descriptions class="margin-top" title="简介" :column="2" border>
        <template slot="extra">
          <el-button type="primary" size="small">操作</el-button>
        </template>
        <el-descriptions-item>
          <template #label>
            <div class="cell-item">
            <el-icon :style="iconStyle">
              <Picture />
            </el-icon>
            头像
            </div>
          </template>
          <img class="img" :src="avatar" alt="" />
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label>
            <div class="cell-item">
            <el-icon :style="iconStyle"><user /></el-icon>
            账户名
            </div>
          </template>
          {{ id }}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label>
            <div class="cell-item">
            <el-icon :style="iconStyle">
              <UserFilled />
            </el-icon>
            昵称
            </div>
          </template>
          {{ nickname }}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label>
            <div class="cell-item">
            <el-icon :style="iconStyle">
              <Odometer />
            </el-icon>
            生日
            </div>
          </template>
          {{ birthday }}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label>
            <div class="cell-item">
            <el-icon :style="iconStyle">
              <Male /><Female />
            </el-icon>
            性别
            </div>
          </template>
          <el-tag size="small">{{ sex }}</el-tag>
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label>
            <div class="cell-item">
            <el-icon :style="iconStyle">
              <Message />
            </el-icon>
            邮箱Email
            </div>
          </template>
          {{ email }}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label>
            <div class="cell-item">
            <el-icon :style="iconStyle">
              <iphone />
            </el-icon>
            手机号码
            </div>
          </template>
          {{ mobilePhoneNumber }}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label>
            <div class="cell-item">
            <el-icon :style="iconStyle">
              <Location />
            </el-icon>
            地区
            </div>
          </template>
          {{ location }}
          <!--
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label>
            <div class="cell-item">
            <el-icon :style="iconStyle">
              <OfficeBuilding />
            </el-icon>
            职业
            </div>
          </template>
          {{ work }}
        </el-descriptions-item>

        <el-descriptions-item>
          <template #label>
            <div class="cell-item">
            <el-icon :style="iconStyle">
              <basketball />
            </el-icon>
            兴趣爱好
            </div>
          </template>
          {{ hobby }}-->
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label>
            <div class="cell-item">
            <el-icon :style="iconStyle">
              <MagicStick />
            </el-icon>
            个性签名
            </div>
          </template>
          {{ signature }}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label>
            <div class="cell-item">
            <el-icon :style="iconStyle">
              <Calendar />
            </el-icon>
              注册日期
            </div>
          </template>
          {{ created_time }}
        </el-descriptions-item>
      </el-descriptions>
    </el-card>
  </div>
</template>

  <script>
import axios from 'axios';

  export default {
    name: "Info",
    data() {
      return {
        avatar: String,
        id:String,
        email: String,
        nickname: String,
        sex: String,
        signature: String,
        birthday: Date,
        mobilePhoneNumber: String,
        location: String,
        created_time: Date,
      }
    },
    mounted() {
      this.load();
    },
    methods: {
      load() {
        let x = new FormData();
      x.append("up_user_id", this.$route.params.id)
      axios.post('http://127.0.0.1:8000/api/up_all_list/', x).then(res => {
            this.avatar = res.data.avatar_url;
            this.id = res.data.id;
            this.birthday = res.data.birthday;
            this.email = res.data.email;
            this.mobilePhoneNumber = res.data.mobilePhoneNumber;
            this.location = res.data.location;
            this.created_time = res.data.created_time;
            this.nickname = res.data.nickname;
            this.sex = res.data.sex ;
            this.signature = res.data.signature;
          })
          .catch((err) => {
            console.log(err);
          });
      },
    },
  };
  </script>
  
  <style scoped>
  .img {
    width: 80px;
    height: 80px;
  }
  </style>