// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css' //ui
import App from './App'
import router from './router'
import axios from 'axios'  
import VueLazyload from 'vue-lazyload'


Vue.prototype.$http = axios  //跨域axios
  
// 懒加载
Vue.use(VueLazyload,{
  error:'/static/images/error.jpg',//图片加载失败时候显示的图片
  loading:'/static/images/loading.gif'//图片还未加载完成时候的loading图片
})


//更换标题
import VueWechatTitle from 'vue-wechat-title'
Vue.use(VueWechatTitle)

Vue.config.productionTip = false
Vue.use(ElementUI)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})


