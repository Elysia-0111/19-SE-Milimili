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
          {{ account }}
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
            年龄
            </div>
          </template>
          {{ age }}
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
          {{ area }}
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
          {{ hobby }}
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
          {{ design }}
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
          {{ createDate | formatDate }}
        </el-descriptions-item>
      </el-descriptions>
    </el-card>
  </div>
</template>

  <script>
  /*import { userInfo } from "@/api/user.js";
  export default {
    name: "Info",
    data() {
      return {
        avatar: String,
        account: String,
        age: Number,
        email: String,
        mobilePhoneNumber: String,
        area: String,
        createDate: Number,
        nickname: String,
        sex: String,
        work: String,
        hobby: String,
        design: String,
      };
    },
    mounted() {
      this.load();
    },
    methods: {
      load() {
        userInfo(this.$route.params.id)
          .then((res) => {
            this.avatar = res.data.avatar;
            this.account = res.data.account;
            this.age = res.data.age;
            this.email = res.data.email;
            this.mobilePhoneNumber = res.data.mobilePhoneNumber;
            this.area = res.data.area;
            this.createDate = res.data.createDate;
            this.nickname = res.data.nickname;
            this.sex = res.data.sex == 1 ? "男" : "女";
            this.work = res.data.work;
            this.design = res.data.design;
            this.hobby = res.data.hobby;
          })
          .catch((err) => {
            console.log(err);
          });
      },
    },
  };*/
  </script>
  
  <style scoped>
  .img {
    width: 80px;
    height: 80px;
  }
  </style>
  