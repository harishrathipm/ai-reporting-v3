import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import Chat from './Chat';

jest.mock('../api/ChatAPI', () => ({
  sendMessage: jest.fn((message) => {
    if (message === 'error') {
      return Promise.reject(new Error('Test error'));
    }
    return Promise.resolve({
      insights: 'Test insights',
      visualization: { data: {}, options: {} },
      data: [],
    });
  }),
}));

describe('Chat', () => {
  it('renders user message and bot response', async () => {
    render(<Chat />);

    const input = screen.getByPlaceholderText('Type your message...');
    const sendButton = screen.getByText('Send');

    fireEvent.change(input, { target: { value: 'Hello' } });
    fireEvent.click(sendButton);

    expect(await screen.findByText('Hello')).toBeInTheDocument();
    expect(await screen.findByText('Test insights')).toBeInTheDocument();
  });

  it('renders error message on API failure', async () => {
    render(<Chat />);

    const input = screen.getByPlaceholderText('Type your message...');
    const sendButton = screen.getByText('Send');

    fireEvent.change(input, { target: { value: 'error' } });
    fireEvent.click(sendButton);

    expect(
      await screen.findByText('Failed to fetch response. Please try again.')
    ).toBeInTheDocument();
  });
});
