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
    path: '/personal/upload',
    name: 'personaldia',
    component: () => import('../views/person/UpLoad.vue')
  },
  {
    path: '/home',
    name: 'videohome',
    component: () => import('../views/video/VideoHome.vue')
  },

  {
    path: '/search',
    name: 'search',
    component: () => import('../views/video/search/SearchComponent.vue')
  },
  {
    path: '/search/video',
    name: 'videosearch',
    // component: () => import('../views/video/Search.vue'),
    component: () => import('../views/video/search/VideoSearch/VideoSearch.vue')
  },
  {
    path: '/search/all',
    name: 'allsearch',
    component: () => import('../views/video/search/AllSearch/AllSearch.vue')
  },
  {
    path: '/search/all/all',
    name: 'allsearchall',
    component: () => import('../views/video/search/AllSearch/AllSearchAll.vue')
  },
  {
    path: '/search/all/maxclick',
    name: 'allsearchmaxclick',
    component: () => import('../views/video/search/AllSearch/AllSearchMaxclick.vue')
  },
  {
    path: '/search/all/newest',
    name: 'allsearchnewest',
    component: () => import('../views/video/search/AllSearch/AllSearchNewest.vue')
  },
  {
    path: '/search/video/all',
    name: 'videosearchall',
    component: () => import('../views/video/search/VideoSearch/VideoSearchAll.vue')
  },
  {
    path: '/search/video/maxlike',
    name: 'videosearchmaxlike',
    component: () => import('../views/video/search/VideoSearch/VideoSearchMaxlike.vue')
  },
  {
    path: '/search/video/newest',
    name: 'videosearchnewest',
    component: () => import('../views/video/search/VideoSearch/VideoSearchNewest.vue')
  },
  {
    path: '/search/user',
    name: 'usersearch',
    component: () => import('../views/video/search/UserSearch/UserSearch.vue')
  },
  {
    path: '/search/user/default',
    name: 'usersearchdefault',
    component: () => import('../views/video/search/UserSearch/UserSearchDefault.vue')
  },
  {
    path: '/search/user/down',
    name: 'usersearchdown',
    component: () => import('../views/video/search/UserSearch/UserSearchDown.vue')
  },
  {
    path: '/search/user/up',
    name: 'usersearchup',
    component: () => import('../views/video/search/UserSearch/UserSearchUp.vue')
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
