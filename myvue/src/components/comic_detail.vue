<template>
    
<div>
    <el-divider>

<el-tooltip content="Comic" placement="top" effect="light"><router-link style=" text-decoration: none;color:black;"  v-bind:to="'/comic'"><i style="font-size:30px;" class="el-icon-notebook-2"></i></router-link></el-tooltip>

</el-divider>

<div class="chapter">

    <div class="top">
   <div style="font-size:30px;margin-bottom: 15px;"> {{ items.title }}</div>
  <div style="margin-left:30px;"> <img class="cover" v-bind:src="cover"></div>
   <span style="margin-left:30px;"> {{ items.author  }}  |</span><span> {{ items.state }} </span>
  
    </div>
 <el-divider></el-divider>

<div class="body">
    <router-link style=" text-decoration: none;color:black;" v-for="chapter in item"
    v-bind:key="chapter.id"  v-bind:to="'/comic/'+ title + '/' + chapter.chapter">
<el-alert
    class="fang"
    
    v-bind:title="chapter.chapter"
    type="info"
    effect="dark"
    center
    :closable="false">
   
  </el-alert>
    </router-link>
</div>
 





</div>


</div>
</template>


<script>
export default {
    data(){
        return{
            title:this.$route.params.title, //url上的传值title
            id:this.$route.params.id, 
            item:[], //chapter
            items:{}, //comic
            cover:"/static/images/cover.jpg",
        }
       
    },
    created() {
        this.getData()
        this.getComic()
    },
    methods: {
        getData(){
            this.$http.get("http://localhost:8000/api/chapter?comic="+ this.title).then(response =>{
            this.item = response.data;
            })
        },
        getComic(){
             this.$http.get("http://localhost:8000/api/comic/"+ this.id +"/").then(response =>{
            this.items = response.data;
            })
        }

    },
}
</script>

<style>
.top{
    height: 260px;
    text-align: left;
    padding: 10px;
}
.cover{
     width: 150px;
    height: 200px;
}
.chapter{
    width: 80%;
    margin-left: 10%;
}
.fang{
    width: 200px;
    margin: 10px;
    float: left;
}


</style>


