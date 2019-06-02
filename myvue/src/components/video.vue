<template>

<div>
  <!-- 导航，提示 -->
<el-divider>
<el-tooltip content="Home" placement="top" effect="light">  <router-link style=" text-decoration: none;color:black;"  v-bind:to="'/'"><i style="font-size:30px;" class="el-icon-s-home"></i></router-link></el-tooltip>
<el-tooltip content="Video" placement="top" effect="light"><router-link style=" text-decoration: none;color:black;"  v-bind:to="'/video'"><i style="font-size:30px;" class="el-icon-monitor"></i></router-link></el-tooltip>
<el-tooltip content="Comic" placement="top" effect="light"><router-link style=" text-decoration: none;color:black;"  v-bind:to="'/comic'"><i style="font-size:30px;" class="el-icon-notebook-2"></i></router-link></el-tooltip>
</el-divider>
<div class="ff">

<el-card class="card" v-for='item in items' v-bind:key="item.id" :body-style="{ padding: '0px' }" shadow="hover">

      <router-link  v-bind:to="'/video/'+ item.id"><img v-bind:src="media + item.cover" class="image"></router-link>
      <div  class="bott">
        <span  style="#">
          <router-link style=" text-decoration: none;"  v-bind:to="'/video/'+ item.id">
          <p class="cut">{{item.title}}</p></router-link>
          </span>

         <i style="float:left" class="co-sm  el-icon-video-play">--0--</i>  <span style="float:right" class="co-sm"> {{ item.video_type }} </span>
      </div>



    </el-card>


</div>

<el-divider></el-divider>
<br>
</div>

</template>


<script>

export  default{
	data(){
		return{
    items:[],
    media:"http://localhost:8000/media/",
		}
    },
    created () {
    this.getData()
  },
  
	methods:{
		getData () {
			this.$http.get("http://localhost:8000/api/video/").then(response =>{
        this.items = response.data;
				console.log(response.data);
			})
			.catch(function(error){
				console.log(error)
			})
		}
	}
}


</script>

<style>
.image{

  width: 100%;
 
}
.card{
  padding: 0px;
  margin: 2.25%;
  width: 20%;
  display: flex;
}
.ff{
  padding-left: 10px;
  width:80%;
  margin-left: 10%;
  flex-wrap:wrap;
  display: flex;
}
.bott{
  height: 30%;

}
.co-sm{
  color:#909399;
  font-size: 13px;
  margin: 5px;
 
}
.cut{
    margin-left: 3%;
    text-align: left;
    color: black;
    font-size: 15px;
    font-weight: 600;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
}
</style>


