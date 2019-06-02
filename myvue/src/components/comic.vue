<template>
<div><el-divider>
<el-tooltip content="Home" placement="top" effect="light">  <router-link style=" text-decoration: none;color:black;"  v-bind:to="'/'"><i style="font-size:30px;" class="el-icon-s-home"></i></router-link></el-tooltip>
<el-tooltip content="Comic" placement="top" effect="light"><router-link style=" text-decoration: none;color:black;"  v-bind:to="'/comic'"><i style="font-size:30px;" class="el-icon-notebook-2"></i></router-link></el-tooltip>
<el-tooltip content="Video" placement="top" effect="light"><router-link style=" text-decoration: none;color:black;"  v-bind:to="'/video'"><i style="font-size:30px;" class="el-icon-monitor"></i></router-link></el-tooltip>
</el-divider>
<br>
    <el-card class="box-card  card-fix">
  <div  slot="header" class="clearfix ">
    <span style=" font-weight: bold; color:black;">最新漫画&nbsp;<i class="el-icon-loading"></i></span>

  </div>
    <el-collapse accordion>
  <el-collapse-item   v-for="(item, index) in items" v-bind:key="index" solt='title'>
      <template style=" font-weight: bold;" slot="title">
  <router-link style=" text-decoration: none;"  v-bind:to="'/comic/'+ item.title +'-' + item.id">
   <p style=" font-weight: bold; color:black;"> {{  item.title  }} &nbsp; <i class="el-icon-share"></i> </p></router-link>
    </template>
    <div style=" font-weight: bold;"> 介绍： </div>
    <div>{{ item.intro }}</div>

  </el-collapse-item>
    </el-collapse>
    </el-card>

    <br>
    <el-divider></el-divider>
    </div>
</template>


<script>
  export default {
    data() {
      return {
    
        items:[],
      };

    },
     created () {
    this.getData()
  },
  
	methods:{
		getData () {
			this.$http.get("http://localhost:8000/api/comic/").then(response =>{
            this.items = response.data;
			
			})
			.catch(function(error){
				console.log(error)
			})
		}
	}

  }
</script>

<style>
.card-fix{
    width: 40%;

    margin-left: 10%;
    text-align: left;

}
</style>
