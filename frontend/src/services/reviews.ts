import axios from "axios";

const axiosInstance = axios.create({
  baseURL: process.env.BACKEND_BASE_URL,
});

interface Review {
  id?: number;
  reviewer: string;
  review_comment: string;
  review_date: string;
}

class ReviewsService {
  getReviews = async () => {
    const response = await axiosInstance.get("reviews");
    return response.data;
  };

  getReview = async (id: string) => {
    const response = await axiosInstance.get(`reviews/${id}`);
    return response.data;
  };

  createReview = async (review: Review) => {
    const response = await axiosInstance.post("reviews", review);
    return response.data;
  };

  updateReview = async (id: number, review: Review) => {
    const response = await axiosInstance.put(`reviews/${id}`, review);
    return response.data;
  };

  deleteReview = async (id: number) => {
    const response = await axiosInstance.delete(`reviews/${id}`);
    return response.data;
  };

  getReviewClassifiers = async () => {
    const response = await axiosInstance.get("reviews/classifiers");
    return response.data;
  };
}

export default new ReviewsService();
