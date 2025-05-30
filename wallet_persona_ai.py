import pandas as pd
import json
from dataLoading import load_wallet_data, extract_wallet_features, classify_wallet
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login


class WalletPersonaGenerator:
    def __init__(self, hf_token=None):
        """Initialize with the Mistral-7B-Instruct-v0.2 model
        
        Args:
            hf_token: Hugging Face API token for authentication (optional for this model)
        """
        if hf_token:
            login(token=hf_token, write_permission=False)

        try:
            print("Loading Mistral model pipeline...")
            model_id = "mistralai/Mistral-7B-Instruct-v0.2"
            self.tokenizer = AutoTokenizer.from_pretrained(model_id)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_id,
                device_map="auto",
                torch_dtype="auto"
            )
            print("Model loaded successfully")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise

    def generate_persona(self, wallet_data, detailed=True):
        """Generate a persona using Mistral-7B model."""
        classifications = wallet_data.get('classifications', [])
        short_addr = f"{wallet_data['address'][:6]}...{wallet_data['address'][-4:]}"
        
        if detailed:
            content = (
                f"Generate a detailed persona profile for crypto wallet {short_addr} based on the following on-chain data:\n"
                f"- Total networth: ${wallet_data.get('total_networth', 0):,.2f}\n"
                f"- Native balance: {wallet_data.get('native_balance', 0):,.2f}\n"
                f"- Token balance: ${wallet_data.get('token_balance_usd', 0):,.2f}\n"
                f"- Chain: {wallet_data.get('chain', 'unknown')}\n"
                f"- Wallet Health Score: {wallet_data.get('wallet_health_score', 0)} / 100\n"
                f"- Risk Score: {wallet_data.get('risk_score', 0)} / 100 (higher means riskier)\n"
                f"- Activity Score: {wallet_data.get('activity_score', 0)} (aggregate transaction count)\n"
                f"- Token Count: {wallet_data.get('token_count', 0)} tokens held\n"
                f"- Top Tokens: {', '.join(wallet_data.get('top_tokens', [])) or 'None'}\n"
                f"- DeFi Protocols: {wallet_data.get('defi_protocols', 0)} engaged\n"
                f"- Total DeFi USD: ${wallet_data.get('total_defi_usd', 0):,.2f}\n"
                f"- NFT Collections: {wallet_data.get('unique_nft_collections', 0)}\n"
                f"- Classifications: {', '.join(classifications) if classifications else 'None'}\n"
                f"- Social Handle: {wallet_data.get('social_handle', 'N/A')}\n"
                f"\nFictional Persona Journey:\n{wallet_data.get('persona_journey', '')}\n\n"
                f"Based on these, create a rich, fictional persona including:\n"
                f"1. Crypto Identity: Who they are in the crypto ecosystem\n"
                f"2. Trading Style: Their approach, time horizon, transaction patterns\n"
                f"3. Risk Profile: Their comfort with different types of risk\n"
                f"4. Blockchain Preferences: Why they choose this chain\n"
                f"5. Personalized Recommendations: 3-4 specific products or strategies\n\n"
                f"Format your response as a well-structured markdown document with headers for each section."
            )
        else:
            content = (
                f"Create a brief crypto persona for wallet {short_addr} with "
                f"${wallet_data.get('total_networth', 0):,.2f} total worth on {wallet_data.get('chain', 'unknown')} chain. "
                f"Include identity type, risk profile, and 1-2 recommendations."
            )

        messages = [{"role": "user", "content": content}]
        print("Generating response with Mistral model...")

        max_new_tokens = 800 if detailed else 300

        input_ids = self.tokenizer.apply_chat_template(
            messages,
            return_tensors="pt"
        ).to(self.model.device)

        # Robust attention_mask and pad_token_id handling
        pad_token_id = self.tokenizer.pad_token_id
        if pad_token_id is None:
            pad_token_id = self.tokenizer.eos_token_id
        attention_mask = (input_ids != pad_token_id).long()
        generated_ids = self.model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_new_tokens=max_new_tokens,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=pad_token_id
        )

        generated_text = self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)

        user_content = messages[-1]["content"]

        if user_content in generated_text:
            response_start = generated_text.find(user_content) + len(user_content)
            response_text = generated_text[response_start:].strip()
            response_text = response_text.replace("[/INST]", "").strip()
        else:
            response_text = generated_text.strip()

        return response_text
