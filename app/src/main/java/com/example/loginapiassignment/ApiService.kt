package com.example.loginapiassignment

import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST

data class User(
    val username: String? = null,
    val email: String? = null,
    val password: String
)

interface ApiService {
    @POST("api/users/signup/")  // Ensure the URL path is correct and matches the Django API
    fun signup(@Body user: User): Call<Void>


    @POST("api/users/login/")
    fun login(@Body user: User): Call<Void>

    @POST("api/users/forgot/")  // Updated endpoint
    fun forgotPassword(@Body email: Map<String, String>): Call<Void>

    @GET("api/users/all/")
    fun getAllUsers(): Call<List<User>>
}
