import { TestLabSeliniumPage } from './app.po';

describe('test-lab-selinium App', () => {
  let page: TestLabSeliniumPage;

  beforeEach(() => {
    page = new TestLabSeliniumPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
