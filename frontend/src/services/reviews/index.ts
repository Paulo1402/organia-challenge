import axios from "axios"
import { Review, ReviewSave } from "./types"

const axiosInstance = axios.create({
  baseURL: process.env.BACKEND_BASE_URL,
})

class ReviewsService {
  async getReviews(): Promise<Review[]> {
    const response = await axiosInstance.get("reviews")
    return response.data
  }

  async getReview(id: number | string): Promise<Review> {
    const response = await axiosInstance.get(`reviews/${id}`)
    return response.data
  }

  async createReview(review: ReviewSave, classifier: string): Promise<Review> {
    const response = await axiosInstance.post("reviews", review, {
      params: { classifier },
    })
    return response.data
  }

  async updateReview(
    id: number | string,
    review: ReviewSave,
    classifier: string
  ): Promise<Review> {
    const response = await axiosInstance.put(`reviews/${id}`, review, {
      params: { classifier },
    })
    return response.data
  }

  async deleteReview(id: number | string): Promise<void> {
    const response = await axiosInstance.delete(`reviews/${id}`)
    return response.data
  }

  async getReviewClassifiers(): Promise<string[]> {
    const response = await axiosInstance.get("reviews/classifiers")
    return response.data
  }
}

export default new ReviewsService()
