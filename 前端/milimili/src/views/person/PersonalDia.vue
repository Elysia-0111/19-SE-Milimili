<template>
  <!-- Form
  <el-dialog
  title="修改个人信息"
  :visible.sync="dialogVisible"
  width="60%"
  :before-close="handleClose"> -->
  <el-dialog v-model="dialogFormVisible" title="修改个人信息" width="60%" :before-close="handleClose">
  <el-form :model="form" :rules="rules" ref="form">
      <div class="updateinfo">
  <div class="left">
      <el-form-item label="头像" prop="avatar">
              <img style="width:150px;height:110px" src="form.avatar_url"/>
          </el-form-item>
            <el-form-item label="账号密码" prop="password">
            <el-input v-model="form.password"></el-input>
          </el-form-item>
          <el-form-item label="昵称" prop="nickname">
            <el-input v-model="form.nickname"></el-input>
          </el-form-item>
          <el-form-item label="生日" prop="birthday">
            <el-input v-model="form.birthday"></el-input>
          </el-form-item>
          <el-form-item label="性别" prop="sex">
            <el-switch
              v-model="form.sex"
              active-color="#13ce66"
              inactive-color="#ff4949"
              active-text="男"
              inactive-text="女"
              :active-value= "1"
               :inactive-value= "0"
            >
            </el-switch>
          </el-form-item>
          <el-form-item label="邮箱" prop="email">
            <el-input v-model="form.email"></el-input>
          </el-form-item>
          
  </div>
  <div class="right">
      <el-form-item label="用户编号" prop="id">
            <el-input v-model="form.id" disabled></el-input>
          </el-form-item>
          <el-form-item label="账号" prop="account">
            <el-input v-model="form.account" disabled></el-input>
          </el-form-item>
          <el-form-item label="地区" prop="area">
            <el-input v-model="form.area"></el-input>
          </el-form-item>
          <el-form-item label="兴趣爱好" prop="hobby">
            <el-input v-model="form.hobby"></el-input>
          </el-form-item>
          <el-form-item label="职业" prop="work">
            <el-input v-model="form.work"></el-input>
          </el-form-item>
            <el-form-item label="个性签名" prop="design">
            <el-input v-model="form.signature"></el-input>
          </el-form-item>
          <el-form-item label="手机号码" prop="mobilePhoneNumber">
            <el-input v-model="form.mobilePhoneNumber"></el-input>
          </el-form-item>
  </div>
  </div>
  </el-form>
  <span slot="footer" class="dialog-footer">
    <!--<el-button @click="handleClose">取 消</el-button>
    <el-button type="primary" @click="submit">提 交</el-button>-->
    <el-button @click="dialogFormVisible=false">取 消</el-button>
    <el-button type="primary" @click="dialogFormVisible=false">提 交</el-button>
  </span>
</el-dialog>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        avatar_url: "",
        password: "",
        nickname: "",
        birthday: Date,
        email: "",
        mobilePhoneNumber: "",
        sex: Number,
        id: Number,
        account: "",
        location: "",
        signature: "",
      },
      dialogFormVisible:true,
      rules: {
        nickname: [
          { required: true, message: "昵称不能为空", trigger: "blur" },
        ],
        password: [
          { required: true, message: "账号密码不能为空", trigger: "blur" },
        ],
      },
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    open() {
      this.dialogVisible = true;
    },
    load() {
      let x = new FormData();
      x.append("up_user_id", this.$route.params.id)
      axios.post('/api/up_all_list', x).then(res => {
          console.log(res);
          Object.assign(this.form, res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    submit() {
      axios.post('/api/change_file', this.form).then(res => {
          console.log(res);
          this.dialogVisible = false;
          this.$emit("flesh");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    handleClose() {
      this.dialogVisible = false;
      this.$emit("flesh");
    },
  },
};
</script>

<style scoped>
.updateinfo {
  height: 350px;
  overflow: auto;
}
.left {
  /* width: 330px; */
  float: left;
}
.right {
  overflow: hidden;
}
</style>
