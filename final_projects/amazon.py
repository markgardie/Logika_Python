import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict, Tuple
import time
from dataclasses import dataclass

@dataclass
class CategoryAnalysis:
    name: str
    top_bsr: List[int]
    bottom_bsr: List[int]
    high_demand: bool
    low_competition: bool
    rating: int

class CategoryAnalyzer:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
        
    def get_bsr(self, url: str) -> List[int]:
        try:
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            bsr_element = soup.find('span', string=lambda text: text and 'Best Seller Rank' in text)
            if bsr_element:
                bsr_text = bsr_element.text
                bsr = int(''.join(filter(str.isdigit, bsr_text.split('#')[1].split('in')[0])))
                return bsr
            return None
        except Exception as e:
            print(f"Erro: {e}")
            return None
       
        
    def analyze_category(self, category_url: str, category_name: str) -> CategoryAnalysis:
        """Analyze a single category"""
        try:
            response = requests.get(category_url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all book links
            book_links = soup.find_all('a', {'class': 'a-link-normal'}, href=True)
            top_books = book_links[:4]
            bottom_books = book_links[-4:]
            
            # Get BSR for top books
            top_bsr = []
            for book in top_books:
                book_url = f"https://amazon.com{book['href']}"
                bsr = self.get_bsr_from_page(book_url)
                if bsr:
                    top_bsr.append(bsr)
                time.sleep(1)  # Respect rate limits
            
            # Get BSR for bottom books
            bottom_bsr = []
            for book in bottom_books:
                book_url = f"https://amazon.com{book['href']}"
                bsr = self.get_bsr_from_page(book_url)
                if bsr:
                    bottom_bsr.append(bsr)
                time.sleep(1)  # Respect rate limits
            
            # Analyze category metrics
            good_demand = any(bsr < 1000 for bsr in top_bsr)
            low_competition = all(bsr > 5000 for bsr in bottom_bsr)
            
            # Calculate rating (1-4, where 1 is best)
            rating = 1
            if good_demand and not low_competition:
                rating = 2
            elif not good_demand and low_competition:
                rating = 3
            elif not good_demand and not low_competition:
                rating = 4
                
            return CategoryAnalysis(
                name=category_name,
                top_bsr=top_bsr,
                bottom_bsr=bottom_bsr,
                good_demand=good_demand,
                low_competition=low_competition,
                rating=rating
            )
            
        except Exception as e:
            print(f"Error analyzing category {category_name}: {e}")
            return None

    def analyze_categories(self, categories: Dict[str, str]) -> pd.DataFrame:
        """Analyze multiple categories and return results as a DataFrame"""
        results = []
        
        for name, url in categories.items():
            print(f"Analyzing category: {name}")
            analysis = self.analyze_category(url, name)
            if analysis:
                results.append({
                    'Category': analysis.name,
                    'Top BSRs': analysis.top_bsr,
                    'Bottom BSRs': analysis.bottom_bsr,
                    'Good Demand': analysis.good_demand,
                    'Low Competition': analysis.low_competition,
                    'Rating': analysis.rating
                })
            
        # Create DataFrame and sort by rating
        df = pd.DataFrame(results)
        df = df.sort_values('Rating')
        return df    

    