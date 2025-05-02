import apiClient from './ApiClient';

class ChatAPI {
  static async sendMessage(message) {
    try {
      const response = await apiClient.post('/api/chat', { message });
      return response.data;
    } catch (error) {
      throw error;
    }
  }
}

export default ChatAPI;
