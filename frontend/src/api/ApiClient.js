import axios from 'axios';
import log from 'loglevel';
import config from '../config';

// Configure loglevel
log.setLevel('info');

// Create an Axios instance
const apiClient = axios.create({
  baseURL: config.SERVER_URL,
  timeout: 10000,
});

// Add a request interceptor
apiClient.interceptors.request.use(
  (request) => {
    log.info('Starting Request', request);
    return request;
  },
  (error) => {
    log.error('Request Error', error);
    return Promise.reject(error);
  }
);

// Add a response interceptor
apiClient.interceptors.response.use(
  (response) => {
    log.info('Response:', response);
    return response;
  },
  (error) => {
    log.error('Response Error', error);
    return Promise.reject(error);
  }
);

export default apiClient;
