import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import ResponseRenderer from './ResponseRenderer';

describe('ResponseRenderer', () => {
  it('renders a table when response type is table', () => {
    const response = {
      type: 'table',
      columns: ['Name', 'Age'],
      rows: [
        ['John', 30],
        ['Jane', 25],
      ],
    };

    render(<ResponseRenderer response={response} />);

    expect(screen.getByText('Name')).toBeInTheDocument();
    expect(screen.getByText('John')).toBeInTheDocument();
  });

  it('renders an error message when response type is error', () => {
    const response = {
      type: 'error',
      message: 'An error occurred.',
    };

    render(<ResponseRenderer response={response} />);

    expect(screen.getByText('An error occurred.')).toBeInTheDocument();
  });
});
