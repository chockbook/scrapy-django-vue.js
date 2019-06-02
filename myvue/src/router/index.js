import Vue from 'vue'
import Router from 'vue-router'
import He from '@/components/He'
import video from '@/components/video'
import comic from '@/components/comic'
import video_detail from '@/components/video_detail'
import comic_detail from '@/components/comic_detail'
import comic_page from '@/components/comic_page'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'He',
      component: He,
      meta: {
        title: 'Home'
      }
    },
    {
      path: '/video',
      name:video,
      component: video,
      meta: {
        title: 'Video'
      }
    },
    {
      path: '/comic',
      name: comic,
      component: comic,
      meta:{
        title:'Comic'
      }
    },
    //视频详细，id传值
    {
      path:'/video/:id',
      name:video_detail,
      component:video_detail,
      meta:{
        title:'哎呀(*-*)'
      }
    },
    {
      path:'/comic/:title-:id',
      name:comic_detail,
      component:comic_detail,
      meta:{
        title:'哇哦(*0*)'
      }
    },
    {
      path:'/comic/:title/:chapter',
      name:comic_page,
      component:comic_page,
      meta:{
        title:'抱歉(~·~)'
      }
    },

  ]
})


