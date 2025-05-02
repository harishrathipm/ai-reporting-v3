import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import ErrorMessage from './ErrorMessage';

describe('ErrorMessage', () => {
  it('renders an error message correctly', () => {
    const message = 'An error occurred.';

    render(<ErrorMessage message={message} />);

    expect(screen.getByText(message)).toBeInTheDocument();
  });
});
