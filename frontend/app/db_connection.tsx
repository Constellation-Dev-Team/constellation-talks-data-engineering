import axios from "axios";

const API_URL = `http://localhost:8000`;

const api = {
  get: async (url: string) => {
    return await axios.get(API_URL + url, {
      headers: {
        "Content-Type": "application/json",
      },
    });
  },
  post: async (url: string, data: any) => {
    return await axios.post(API_URL + url, data, {
      headers: {
        "Content-Type": "application/json",
      },
    });
  },
  delete: async (url: string) => {
    return await axios.delete(API_URL + url, {
      headers: {
        "Content-Type": "application/json",
      },
    });
  },
  patch: async (url: string, data: any) => {
    return await axios.patch(API_URL + url, data, {
      headers: {
        "Content-Type": "application/json",
      },
    });
  }
};

export default api;