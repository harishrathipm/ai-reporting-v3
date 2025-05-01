// App.test.js
import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from './App.js';

test('renders welcome message', () => {
  const { getByText } = render(<App />);
  const welcomeElement = getByText(/Welcome to the Frontend/i);
  expect(welcomeElement).toBeInTheDocument();
});
