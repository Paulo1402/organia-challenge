import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "",
        name: "home",
        redirect: { name: "List Reviews" },
      },
      {
        path: "reviews",
        name: "list-reviews",
        component: () => import("@/views/ListReviews.vue"),
      },
      {
        path: "reviews/new",
        name: "new-review",
        component: () => import("@/views/SaveReview.vue"),
      },
      {
        path: "reviews/:id",
        name: "update-review",
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
