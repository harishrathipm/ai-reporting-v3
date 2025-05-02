import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import ImageRenderer from './ImageRenderer';

describe('ImageRenderer', () => {
  it('renders an image with the correct src and alt attributes', () => {
    const src = 'https://via.placeholder.com/150';
    const alt = 'Placeholder Image';

    render(<ImageRenderer src={src} alt={alt} />);

    const image = screen.getByAltText(alt);
    expect(image).toBeInTheDocument();
    expect(image).toHaveAttribute('src', src);
  });
});
