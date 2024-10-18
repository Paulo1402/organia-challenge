import axios from "axios";
import { Review, ReviewCreate } from "./types";

const axiosInstance = axios.create({
  baseURL: process.env.BACKEND_BASE_URL,
});

class ReviewsService {
  getReviews = async () => {
    const response = await axiosInstance.get("reviews");
    return response.data;
  };

  getReview = async (id: number | string) => {
    const response = await axiosInstance.get(`reviews/${id}`);
    return response.data;
  };

  createReview = async (review: ReviewCreate) => {
    const response = await axiosInstance.post("reviews", review);
    return response.data;
  };

  updateReview = async (id: number | string, review: Review) => {
    const response = await axiosInstance.put(`reviews/${id}`, review);
    return response.data;
  };

  deleteReview = async (id: number | string) => {
    const response = await axiosInstance.delete(`reviews/${id}`);
    return response.data;
  };

  getReviewClassifiers = async () => {
    const response = await axiosInstance.get("reviews/classifiers");
    return response.data;
  };
}

export default new ReviewsService();
