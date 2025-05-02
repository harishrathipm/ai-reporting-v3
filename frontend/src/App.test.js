// App.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from './App';

describe('App', () => {
  it('renders the Chat component', () => {
    render(<App />);
    expect(
      screen.getByPlaceholderText('Type your message...')
    ).toBeInTheDocument();
  });
});
