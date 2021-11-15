import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Pay from '@/components/Pay'
import Receive from '@/components/Receive'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/pay',
      name: 'pay',
      component: Pay
    },
    {
      path: '/receive',
      name: 'receive',
      component: Receive
    }
  ]
})
