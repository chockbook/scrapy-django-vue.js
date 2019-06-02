<template>
    <div>
<el-divider>

<el-tooltip content="Comic" placement="top" effect="light"><router-link style=" text-decoration: none;color:black;"  v-bind:to="'/comic'"><i style="font-size:30px;" class="el-icon-notebook-2"></i></router-link></el-tooltip>

</el-divider>

<div class="cc">
{{chapter }}
</div>

<div v-for="img in imglist" v-bind:key="img.page">
<img  v-lazy="media + img.page_path" alt="img">
</div>
    </div>
</template>
<style>
.c{
    
    margin: 5px;
    font-size: 15px;
    font-weight: bold;
}
.cc{
        font-size: 20px;
    margin-bottom: 20px;
}
img{
    width: 800px;
}

</style>
<script>
export default {
    data(){
        return{
            media:"http://localhost:8000/media/",
            chapter:this.$route.params.chapter,
            imglist:[],
            comic:this.$route.params.title
      

        }
    },
    //"http://localhost:8000/api/page?chapter="  +  chapter

    created() {
        this.getData()
    },
    methods: {
        getData(){
            this.$http.get("http://localhost:8000/api/page?chapter=" + this.chapter).then(response =>{
            this.imglist = response.data;
            })
        }
    },

}
</script>

