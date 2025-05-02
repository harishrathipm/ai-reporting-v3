import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import LoadingSpinner from './LoadingSpinner';

describe('LoadingSpinner', () => {
  it('renders a loading spinner', () => {
    const { container } = render(<LoadingSpinner />);
    expect(container).toBeInTheDocument();
  });
});
