import Vue from 'vue'
import Router from 'vue-router'
import Init from '@/components/Init'
import Pay from '@/components/Pay'
import Receive from '@/components/Receive'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'init',
      component: Init
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
