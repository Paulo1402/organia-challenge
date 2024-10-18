export interface Review {
  id: number
  reviewer: string
  review_comment: string
  review_date: string
  review_classifier: string
  review_classification: string
}

export type ReviewCreate = Omit<
  Review,
  "id" | "review_classifier" | "review_classification"
>
