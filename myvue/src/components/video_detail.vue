<template>
<div >
    <el-divider>
<el-tooltip content="Video" placement="top" effect="light">
    <router-link style=" text-decoration: none;color:black;"  v-bind:to="'/video'">
    <i style="font-size:30px;" class="el-icon-monitor"></i>
    </router-link>
    </el-tooltip>
    </el-divider>
<br>
<div class="back">
<div class="vid ">
 <d-player  ref="player" :options="options"></d-player>
 </div>
</div>
<div class="xbody el-card__body is-always-shadow">

<div class="title">{{ item.title }} </div>
<el-divider></el-divider>
<div class="content">
  <div class="type">分类： {{item.video_type}} </div>
  <time class="time">   <i class="el-icon-alarm-clock" ></i>   {{ item.create_time }}</time>
   </div>


</div>
<br>
<el-divider></el-divider>

 </div>
</template>

<script type="text/ecmascript-6">
import dPlayer from 'vue-dplayer'
import 'vue-dplayer/dist/vue-dplayer.css'

//bug Chrome浏览器下视频不能快进。

export  default{
    
    name: 'in-video',
	data(){
		return{
        id :this.$route.params.id,
        item : {},
        media:"http://localhost:8000/media/",
        cid:'', //新video-URL
        player: null,
        //dpalyer设置，具体看官方文档。
        options: {
          preload: 'auto',
        aspectRatio: '4:3',
          video: {
            url: '',//由于URL刚开始为空，后面需要用到  switchVideo进行URL切换
          
          },
          contextmenu: [
            {text: 'custom2',
            click: (player) => {
                console.log(player);//自定义contextmenu
            }}
          ]
        }
		}
    },
  
    mounted() {
    this.getData()
    this.player = this.$refs.player.dp  
  },
	methods:{
		getData () {
       
			      this.$http.get("http://localhost:8000/api/video/"+ this.id).then(response =>{
            this.item = response.data;
            this.cid = this.media + response.data['video']
            console.log(this.cid);
            }).then(response =>{
                 this.player.switchVideo({
                  url: this.cid,            
            })
          })
			.catch(function(error){
				console.log(error)
			})
        },
    },


    components: {
      dPlayer
    }

  }

</script>


<style>
.back{
    background-color: rgb(221, 233, 233)
}
.vid{
    width: 50%;
    margin-left: 25%;
    
}
.xbody{
  width: 70%;
  margin-left: 15%;
  margin-top: 50px;
      border: 1px solid #EBEEF5;
      border-radius: 4px;
      
}
.title{
  text-align: left;
  font-size: 25px;
  font-weight:bold; 
  margin-bottom: 20px;
}
.type{
    text-align: left;
}
 .time {
    font-size: 13px;
    color: #999;
    float: right;
  }
  
</style>

