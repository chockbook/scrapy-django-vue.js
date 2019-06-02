<template>
<div>

  <div>

<img class="aa" src="/static/images/home.jpg" alt="">

</div>



<div>
<el-divider>
<el-tooltip content="Home" placement="top" effect="light"><router-link style=" text-decoration: none;color:black;"  v-bind:to="'/'"><i style="font-size:40px;" class="el-icon-s-home"></i></router-link></el-tooltip>
</el-divider><br><el-divider>
<el-tooltip content="漫画" placement="top" effect="light"><router-link style=" text-decoration: none;color:black;"  v-bind:to="'/comic'"><i style="font-size:40px;" class="el-icon-notebook-2"></i></router-link></el-tooltip>
</el-divider><br><el-divider>
<el-tooltip content="视频" placement="top" effect="light"><router-link style=" text-decoration: none;color:black;"  v-bind:to="'/video'"><i style="font-size:40px;" class="el-icon-monitor"></i></router-link></el-tooltip>
</el-divider>

</div>
<br>
<el-divider></el-divider>
</div>
</template>
<style>
body {
  text-align: center;
}
.aa{
  border-radius: 10px;
  width: 600px;
  margin-top: -20px;
  margin-bottom: 40px;
}
.rute{

  width:100px;
  height: 100px;
  background-color: antiquewhite;
  border-radius: 90%;
}


</style>

<script>

export default {
  data() {
    return {
      currentDate: new Date()
    };
  }
}


</script>
