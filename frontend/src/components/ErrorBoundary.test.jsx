import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import ErrorBoundary from './ErrorBoundary';

function ProblematicComponent() {
  throw new Error('Test error');
}

describe('ErrorBoundary', () => {
  it('renders fallback UI when an error is thrown', () => {
    render(
      <ErrorBoundary>
        <ProblematicComponent />
      </ErrorBoundary>
    );

    expect(screen.getByText('Something went wrong.')).toBeInTheDocument();
  });

  it('renders children when no error is thrown', () => {
    render(
      <ErrorBoundary>
        <div>All good!</div>
      </ErrorBoundary>
    );

    expect(screen.getByText('All good!')).toBeInTheDocument();
  });
});
