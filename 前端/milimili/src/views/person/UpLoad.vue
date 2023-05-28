<template>
    <div class="upload">
        <el-container >
            <el-header style="box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);height: 75px;">
                <el-row>
                    <el-col :span="2" :offset="1"><router-link to="/video/home"><a
                                class="fonthead">首页</a></router-link></el-col>
                    <el-col :span="18"></el-col>
                    <el-col :span="1"><router-link to="/personal">
                            <img class="img1" src="../../assets/img/V.png">
                        </router-link>
                    </el-col>
                </el-row>
            </el-header>
            <el-main>
                <el-col :span="6" :offset="9"></el-col>
                <el-upload
  action="http://localhost:8081/personal/upload"
  list-type="picture-card"
  :auto-upload="false"
  :on-preview="handlePreview"
  :on-remove="handleRemove">
    <i slot="default" class="el-icon-plus"></i>
    <i class="el-icon-upload"></i>
    <div class="el-upload__text"><em>点击上传</em></div>
    <div slot="file" slot-scope="{file}">
      <img
        class="el-upload-list__item-thumbnail"
      >
      <span class="el-upload-list__item-actions">
        <span
          class="el-upload-list__item-preview"
          @click="handlePictureCardPreview(file)"
        >
          <i class="el-icon-zoom-in"></i>
        </span>
        <span
          v-if="!disabled"
          class="el-upload-list__item-delete"
          @click="handleDownload(file)"
        >
          <i class="el-icon-download"></i>
        </span>
        <span
          v-if="!disabled"
          class="el-upload-list__item-delete"
          @click="handleRemove(file)"
        >
          <i class="el-icon-delete"></i>
        </span>
      </span>
    </div>
</el-upload>
<el-dialog :visible.sync="dialogVisible">
  <img width="100%" :src="dialogImageUrl" alt="">
</el-dialog>
            </el-main>
        </el-container>
  <div>
  </div>

    </div>
    <el-backtop></el-backtop>
  </template>
  

  <script>
  export default {
    data() {
      return {
        dialogImageUrl: '',
        dialogVisible: false,
        disabled: false
      };
    },
    methods: {
      handleRemove(file) {
        console.log(file);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
      handleDownload(file) {
        console.log(file);
      },
    }
  }
</script>
  
<style scoped>
  .fonthead {
    color: rgb(0, 0, 0);
    font-size: large;
  }

</style>

