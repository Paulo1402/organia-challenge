import axios from "axios";

const axiosInstance = axios.create({
  baseURL: process.env.BACKEND_BASE_URL,
});

class ReviewsService {
  getReviews = async () => {
    const response = await axiosInstance.get("reviews");
    return response.data;
  };

  getReview = async (id: string) => {
    const response = await axiosInstance.get(`reviews/${id}`);
    return response.data;
  };

  createReview = async (review: any) => {
    const response = await axiosInstance.post("reviews", review);
    return response.data;
  };

  updateReview = async (id: string, review: any) => {
    const response = await axiosInstance.put(`reviews/${id}`, review);
    return response.data;
  };

  deleteReview = async (id: string) => {
    const response = await axiosInstance.delete(`reviews/${id}`);
    return response.data;
  };

  getReviewClassifiers = async () => {
    const response = await axiosInstance.get("review/classifiers");
    return response.data;
  };
}

export default new ReviewsService();
