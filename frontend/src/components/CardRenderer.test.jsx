import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import CardRenderer from './CardRenderer';

describe('CardRenderer', () => {
  it('renders a card with title and content', () => {
    const title = 'Card Title';
    const content = 'This is the card content.';

    render(<CardRenderer title={title} content={content} />);

    expect(screen.getByText(title)).toBeInTheDocument();
    expect(screen.getByText(content)).toBeInTheDocument();
  });
});
