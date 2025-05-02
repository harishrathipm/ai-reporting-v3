import apiClient from './ApiClient';
import log from 'loglevel';

class ChatAPI {
  static async sendMessage(message) {
    try {
      const response = await apiClient.post('/api/chat', { message });
      log.info('Server Response:', response.data); // Log the server response
      return response.data;
    } catch (error) {
      log.error('Error in sendMessage:', error);
      throw error;
    }
  }
}

export default ChatAPI;
