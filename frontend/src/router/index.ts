import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "",
        name: "Home",
        component: () => import("@/views/Home.vue"),
      },
      {
        path: "reviews",
        name: "List Reviews",
        component: () => import("@/views/ListReviews.vue"),
      },
      {
        path: "reviews/new",
        name: "New Review",
        component: () => import("@/views/SaveReview.vue"),
      },
      {
        path: "reviews/:id",
        name: "Update Review",
        component: () => import("@/views/SaveReview.vue"),
      }
    ]
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
