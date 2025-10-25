import axios from "axios";
import store from "../store/auth"; 

const api = axios.create({
  baseURL: "http://localhost:8000", 
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});


api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      store.commit("logout");
      window.location.href = "/login";
    }
    return Promise.reject(error);
  }
);

export default api;
