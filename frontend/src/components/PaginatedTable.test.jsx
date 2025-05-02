import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import PaginatedTable from './PaginatedTable';

describe('PaginatedTable', () => {
  const columns = ['Name', 'Age', 'City'];
  const rows = [
    ['John', 30, 'New York'],
    ['Jane', 25, 'Los Angeles'],
    ['Mike', 35, 'Chicago'],
    ['Anna', 28, 'Houston'],
    ['Tom', 40, 'Phoenix'],
  ];

  it('renders table with correct columns and rows', () => {
    render(<PaginatedTable columns={columns} rows={rows} />);

    columns.forEach((column) => {
      expect(screen.getByText(column)).toBeInTheDocument();
    });

    rows.slice(0, 5).forEach((row) => {
      row.forEach((cell) => {
        expect(screen.getByText(cell)).toBeInTheDocument();
      });
    });
  });
});
