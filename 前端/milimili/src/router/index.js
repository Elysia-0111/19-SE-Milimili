import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "login" */ '../views/LoginView.vue')
  },
  {
    path: '/video',
    name: 'video',
    component: () => import(/* webpackChunkName: "login" */ '../views/VideoView.vue')
  },
  {
    path: '/login2',
    name: 'login2',
    component: () => import(/* webpackChunkName: "login" */ '../views/Login.vue')
  },
  {
    path: '/homepage',
    name: 'homepage',
    component: () => import(/* webpackChunkName: "login" */ '../views/HomePage.vue')
  },
  {
    path: '/personal',
    name: 'personal',
    component: () => import('../views/person/Personal.vue')
  },
  {
    path: '/personal/info',
    name: 'info',
    component: () => import('../views/person/Info.vue')
  },
  {
    path: '/personal/myarticle',
    name: 'myarticle',
    component: () => import('../views/person/MyArticle.vue')
  },
  {
    path: '/personal/mycollect',
    name: 'mycollect',
    component: () => import('../views/person/MyCollect.vue')
  },
  {
    path: '/personal/myfan',
    name: 'myfan',
    component: () => import('../views/person/MyFanAndFollow.vue')
  },
  {
    path: '/personal/myfollow',
    name: 'myfollow',
    component: () => import('../views/person/MyFanAndFollow.vue')
  },
  {
    path: '/personal/personaldia',
    name: 'personaldia',
    component: () => import('../views/person/PersonalDia.vue')
  },
  {
    path: '/video/home',
    name: 'videohome',
    component: () => import('../views/video/VideoHome.vue')
  }
  /*{
    //path: '/newsuser/personal/:id',
    path: '/personal',
    component: r => require.ensure([], () => r(require('@/views/person/Personal')), 'personal'),
    //meta: {
    //  requireLogin: true
    //},
    children: [
      {
        // path: '/personal/info/:id',
        //path: '/newsuser/personal/info/:id',
        path: '/personal/info',
        name:'info',
        component: r => require.ensure([], () => r(require('@/views/person/Info')), 'info')
      },
      {
        //path:'/newsuser/personal/myarticle/:id',
        path:'/personal/myarticle',
        name:'myarticle',
        component: r => require.ensure([], () => r(require('@/views/person/MyArticle')), 'myarticle')
      },
      {
        //path:'/newsuser/personal/mycollect/:id',
        path:'/personal/mycollect',
        name:'mycollect',
        component: r => require.ensure([], () => r(require('@/views/person/MyCollect')), 'mycollect')
      },
      {
        //path:'/newsuser/personal/myfan/:id',
        path:'/personal/myfan',
        name:'myfan',
        component: r => require.ensure([], () => r(require('@/views/person/MyFanAndFollow')), 'myfan')
      },
      {
        path:'/personal/myfollow',
        name:'myfollow',
        component: r => require.ensure([], () => r(require('@/views/person/MyFanAndFollow')), 'myfollow')
      }
  ]
}*/
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
