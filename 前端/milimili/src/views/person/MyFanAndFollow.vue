<template>
    <div class="fanorfollow_box">
      <div class="fanorfollow">
        <div class="fanorfollow_left">
          <img class="fanorfollow_img" src="@/assets/logo.png" />
        </div>
        <div class="fanorfollow_info">
          <div class="fanorfollow_info_top">
            <span style="color: #666; max-width: 180px">name</span>
          </div>
          <div class="fanorfollow_info_bottom">
            <span >123</span>
          </div>
        </div>
        <div class="fanorfollow_botton">
          <el-button
            type="primary"
            size="small"
            round
            icon="el-icon-check"
            v-text="1 > -1 ? '已关注' : '关注'"
          ></el-button>
        </div>
      </div>
      <div>
        <el-empty
          :image-size="250"
          description="这里什么都没有哟"
        ></el-empty>
      </div>
    </div>
  </template>
  
  <script>  
  export default {
    name: "MyFanAndFollow",
    inject: ["reload"],
    data() {
      return {
        allData: [],
        isfollow: true,
        followData: {
          fanId: "",
          followId: "",
        },
        isfollowid: [],
      };
    },

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
  